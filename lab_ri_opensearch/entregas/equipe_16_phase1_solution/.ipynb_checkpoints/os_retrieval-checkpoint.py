"""Busca lexica/vetorial no OpenSearch; embeddings, RRF e reranking no cliente."""
from __future__ import annotations

import json
import math
import os
import re
import urllib.error
import urllib.request
from pathlib import Path

from ri_core import document_text, load_data, rrf, save_run, sha256, write_json

ROOT = Path(__file__).resolve().parent
DEFAULTS = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))


def validate_config(config):
    if config.get("mode") not in ("lexical", "dense", "rrf", "reranked"):
        raise ValueError("mode invalido")
    if config.get("analyzer") not in ("standard", "portuguese"):
        raise ValueError("analyzer deve ser standard ou portuguese")
    for key in ("bm25_k1", "bm25_b", "title_boost"):
        v = config.get(key)
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
            raise ValueError(f"Parametro numerico invalido: {key}")
    if config["bm25_k1"] <= 0 or not 0 <= config["bm25_b"] <= 1 or config["title_boost"] <= 0:
        raise ValueError("Parametros BM25/title invalidos")
    if type(config.get("candidate_k")) is not int or not 1 <= config["candidate_k"] <= 100:
        raise ValueError("candidate_k deve estar entre 1 e 100")
    if type(config.get("rrf_k")) is not int or config["rrf_k"] < 1:
        raise ValueError("rrf_k deve ser inteiro positivo")
    return config


class OpenSearchHTTP:
    backend = "opensearch"

    def __init__(self, url=None):
        self.url = (url or os.environ.get("OPENSEARCH_URL", "http://127.0.0.1:9200")).rstrip("/")
        if not self.url.startswith(("http://127.0.0.1:", "http://localhost:")):
            raise ValueError("Cliente de referencia requer endpoint HTTP local; para servidor institucional configure TLS/autenticacao")

    def request(self, method, path, body=None, ndjson=False):
        payload = body.encode("utf-8") if ndjson else (json.dumps(body, ensure_ascii=False).encode("utf-8") if body is not None else None)
        req = urllib.request.Request(self.url + path, data=payload, method=method,
            headers={"Content-Type": "application/x-ndjson" if ndjson else "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=180) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            raise RuntimeError(f"OpenSearch HTTP {exc.code}: {exc.read().decode()[:1500]}") from exc

    def check(self):
        info = self.request("GET", "/")
        if info.get("version", {}).get("distribution") != "opensearch" or info["version"]["number"] != DEFAULTS["opensearch_version"]:
            raise ValueError(f"Use OpenSearch {DEFAULTS['opensearch_version']}: {info.get('version')}")
        return info


def index_mapping(config, dimension=None):
    validate_config(config)
    settings = {"number_of_shards": 1, "number_of_replicas": 0,
        "similarity": {"lab_bm25": {"type": "BM25", "k1": config["bm25_k1"], "b": config["bm25_b"]}}}
    properties = {"doc_id": {"type": "keyword"},
        "title": {"type": "text", "analyzer": config["analyzer"], "similarity": "lab_bm25"},
        "text": {"type": "text", "analyzer": config["analyzer"], "similarity": "lab_bm25"}}
    if dimension is not None:
        if type(dimension) is not int or dimension < 1:
            raise ValueError("Dimensao invalida")
        settings["index.knn"] = True
        properties["embedding"] = {"type": "knn_vector", "dimension": dimension,
            "method": {"name": "hnsw", "engine": "lucene", "space_type": "cosinesimil",
                       "parameters": {"ef_construction": 128, "m": 16}}}
    return {"settings": settings, "mappings": {"dynamic": "strict", "properties": properties}}


def valid_vector(vector, dimension):
    if len(vector) != dimension or any(not math.isfinite(float(x)) for x in vector):
        raise ValueError("Vetor nao finito/dimensao incorreta")
    if sum(float(x) ** 2 for x in vector) == 0:
        raise ValueError("Vetor zero nao permitido para cosseno")


def populate_index(client, index, docs, config, vectors=None):
    if not re.fullmatch(r"ri-[a-z0-9_-]{1,150}", index):
        raise ValueError("Nome do indice deve comecar com ri- e conter letras minusculas/numeros/_/-")
    dimension = len(vectors[0]) if vectors is not None and len(vectors) else None
    if vectors is not None and len(vectors) != len(docs):
        raise ValueError("Quantidade de vetores diferente dos documentos")
    if vectors is not None:
        for vector in vectors:
            valid_vector(vector, dimension)
    # Criacao falha se indice ja existir; nunca apaga indice do usuario.
    client.request("PUT", f"/{index}", index_mapping(config, dimension))
    documents = list(docs.values())
    for start in range(0, len(documents), 200):
        lines = []
        for pos in range(start, min(start + 200, len(documents))):
            d = documents[pos]
            lines.append(json.dumps({"index": {"_index": index, "_id": d["doc_id"]}}))
            record = {"doc_id": d["doc_id"], "title": d.get("title", ""), "text": d["text"]}
            if vectors is not None:
                record["embedding"] = [float(v) for v in vectors[pos]]
            lines.append(json.dumps(record, ensure_ascii=False))
        reply = client.request("POST", "/_bulk", "\n".join(lines) + "\n", ndjson=True)
        if reply.get("errors") or any(next(iter(x.values())).get("status", 500) >= 300 for x in reply.get("items", [])):
            raise RuntimeError(f"Falha parcial no bulk: {str(reply)[:1200]}")
        if len(reply.get("items", [])) != min(200, len(documents) - start):
            raise RuntimeError("Resposta bulk com quantidade inesperada")
    client.request("POST", f"/{index}/_refresh")
    count = client.request("GET", f"/{index}/_count")["count"]
    if count != len(docs):
        raise ValueError("Contagem do indice diferente do corpus")
    return {"index": index, "documents": count, "dimension": dimension}


def search(client, index, queries, config, vectors=None):
    k = config["candidate_k"]
    result = {}
    for pos, (qid, query) in enumerate(queries.items()):
        if vectors is None:
            clause = {"multi_match": {"query": query["text"], "fields": [f"title^{config['title_boost']}", "text"]}}
            body = {"size": k, "query": clause, "_source": False,
                    "sort": [{"_score": "desc"}, {"doc_id": "asc"}]}
        else:
            vector = [float(x) for x in vectors[pos]]
            valid_vector(vector, len(vector))
            body = {"size": k, "query": {"knn": {"embedding": {"vector": vector, "k": k}}}, "_source": False}
        response = client.request("POST", f"/{index}/_search", body)
        if response.get("timed_out") or response.get("_shards", {}).get("failed", 0):
            raise RuntimeError("Busca incompleta/timeout no OpenSearch")
        hits = response["hits"]["hits"]
        result[qid] = sorted([(str(h["_id"]), float(h["_score"])) for h in hits], key=lambda p: (-p[1], p[0]))
    return result


class E5Encoder:
    def __init__(self):
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer(DEFAULTS["embedding"], revision=DEFAULTS["embedding_revision"],
                                         device=DEFAULTS["device"], trust_remote_code=False)
        self.model.max_seq_length = DEFAULTS["max_length"]

    def encode(self, texts, query=False):
        prefix = "query: " if query else "passage: "
        return self.model.encode([prefix + t for t in texts], batch_size=DEFAULTS["batch_size"],
                                 normalize_embeddings=True, show_progress_bar=True).tolist()


class NeuralReranker:
    def __init__(self):
        from sentence_transformers import CrossEncoder
        self.model = CrossEncoder(DEFAULTS["reranker"], revision=DEFAULTS["reranker_revision"],
            device=DEFAULTS["device"], max_length=DEFAULTS["max_length"], trust_remote_code=False)

    def predict(self, pairs):
        return self.model.predict(pairs, batch_size=DEFAULTS["batch_size"], show_progress_bar=True).tolist()


def run_experiment(data, out, config, index, client=None, encoder=None, reranker=None, strategies=None):
    from ri_workflow import fresh
    validate_config(config)
    docs, queries = load_data(data)
    target = fresh(out)
    client = client or OpenSearchHTTP()
    info = client.check()
    mode = config["mode"]
    vectors = query_vectors = None
    if mode != "lexical":
        encoder = encoder or E5Encoder()
        vectors = encoder.encode([document_text(d) for d in docs.values()])
        query_vectors = encoder.encode([q["text"] for q in queries.values()], query=True)
    stats = populate_index(client, index, docs, config, vectors)
    lexical = search(client, index, queries, config)
    rankings = lexical
    if mode != "lexical":
        dense = search(client, index, queries, config, query_vectors)
        save_run(target / "dense.csv", "dense", dense)
        if mode == "dense":
            rankings = dense
        elif strategies is None:
            rankings = rrf([lexical, dense], config["rrf_k"], config["candidate_k"])
        else:
            rankings = {qid: strategies.fuse_rankings(lexical[qid], dense[qid], config["rrf_k"], config["candidate_k"])
                        for qid in queries}
    if mode == "reranked":
        reranker = reranker or NeuralReranker()
        reranked = {}
        for qid, hits in rankings.items():
            if not hits:
                reranked[qid] = []
                continue
            if strategies is not None:
                reranked[qid] = strategies.rerank_candidates(queries[qid]["text"], hits, docs, reranker, config["candidate_k"])
            else:
                scores = reranker.predict([(queries[qid]["text"], document_text(docs[did])) for did, _ in hits])
                if len(scores) != len(hits) or any(not math.isfinite(float(s)) for s in scores):
                    raise ValueError("Reranker devolveu scores invalidos")
                reranked[qid] = sorted([(did, float(s)) for (did, _), s in zip(hits, scores)], key=lambda x: (-x[1], x[0]))
        rankings = reranked
    save_run(target / "lexical.csv", "lexical", lexical)
    save_run(target / "run.csv", f"{config['team_id']}_{mode}", rankings)
    meta = {"backend": client.backend, "server": info["version"], "config": config, "index": stats,
            "corpus_sha256": sha256(Path(data) / "corpus.jsonl"),
            "queries_sha256": sha256(Path(data) / "queries.jsonl"), "run_sha256": sha256(target / "run.csv"),
            "models": {k: DEFAULTS[k] for k in ("embedding", "embedding_revision", "reranker", "reranker_revision")}
                      if mode != "lexical" else {}}
    write_json(target / "run.meta.json", meta)
    return meta
