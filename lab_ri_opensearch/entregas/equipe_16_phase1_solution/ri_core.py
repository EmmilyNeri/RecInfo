"""Contratos, BM25, RRF e avaliacao. Sem dependencias externas."""
from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

RUN_FIELDS = ["run_id", "query_id", "doc_id", "rank", "score"]


def read_jsonl(path):
    with open(path, encoding="utf-8-sig") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def write_jsonl(path, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        for row in rows:
            stream.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def read_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or len(set(reader.fieldnames)) != len(reader.fieldnames):
            raise ValueError(f"Cabecalho ausente/duplicado: {path}")
        return list(reader)


def write_csv(path, fields, rows):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def stable_key(seed, identifier):
    return hashlib.sha256(f"{seed}:{identifier}".encode()).hexdigest()


def unique_map(rows, key):
    mapped = {}
    for row in rows:
        identifier = row.get(key)
        if not isinstance(identifier, str) or not identifier.strip():
            raise ValueError(f"ID invalido em {key}: {identifier!r}")
        if identifier in mapped:
            raise ValueError(f"ID duplicado em {key}: {identifier}")
        mapped[identifier] = row
    return mapped


def load_data(folder):
    folder = Path(folder)
    docs = unique_map(read_jsonl(folder / "corpus.jsonl"), "doc_id")
    queries = unique_map(read_jsonl(folder / "queries.jsonl"), "query_id")
    if not docs or not queries:
        raise ValueError("Corpus/consultas vazios")
    for row in docs.values():
        if not isinstance(row.get("text"), str) or not row["text"].strip():
            raise ValueError(f"Texto vazio em {row['doc_id']}")
    for row in queries.values():
        if not isinstance(row.get("text"), str) or not row["text"].strip():
            raise ValueError(f"Consulta vazia em {row['query_id']}")
    return docs, queries


def document_text(row):
    return (row.get("title", "").strip() + "\n" + row["text"].strip()).strip()


def tokenize(text):
    return re.findall(r"\w+", unicodedata.normalize("NFKC", text).casefold(), flags=re.UNICODE)


class BM25:
    """IDF de Robertson suavizado positivo; consulta por termos unicos."""

    def __init__(self, docs, k1=1.2, b=0.75):
        if k1 <= 0 or not 0 <= b <= 1:
            raise ValueError("BM25 exige k1>0 e 0<=b<=1")
        self.k1, self.b = k1, b
        self.postings = defaultdict(list)
        self.lengths = {}
        for doc_id, doc in docs.items():
            tokens = tokenize(document_text(doc))
            self.lengths[doc_id] = len(tokens)
            for term, count in Counter(tokens).items():
                self.postings[term].append((doc_id, count))
        self.n = len(docs)
        self.avgdl = sum(self.lengths.values()) / max(self.n, 1) or 1.0

    def search(self, query, k=100):
        scores = defaultdict(float)
        for term in sorted(set(tokenize(query))):
            postings = self.postings.get(term, [])
            idf = math.log(1 + (self.n - len(postings) + 0.5) / (len(postings) + 0.5))
            for doc_id, tf in postings:
                denom = tf + self.k1 * (1 - self.b + self.b * self.lengths[doc_id] / self.avgdl)
                scores[doc_id] += idf * tf * (self.k1 + 1) / denom
        return sorted(scores.items(), key=lambda item: (-item[1], item[0]))[:k]


def save_run(path, run_id, rankings):
    if not run_id.strip():
        raise ValueError("run_id vazio")
    rows = []
    for qid in sorted(rankings):
        for rank, (doc_id, score) in enumerate(rankings[qid], 1):
            rows.append(dict(run_id=run_id, query_id=qid, doc_id=str(doc_id), rank=rank, score=float(score)))
    write_csv(path, RUN_FIELDS, rows)


def load_run(path, docs, queries, max_rank=100):
    rows = read_csv(path)
    if not rows:
        raise ValueError(f"Run vazio: {path}")
    runs, ids = defaultdict(list), set()
    for row in rows:
        if set(row) != set(RUN_FIELDS):
            raise ValueError(f"Contrato do run deve ser {RUN_FIELDS}")
        ids.add(row["run_id"])
        qid, did = row["query_id"], row["doc_id"]
        if qid not in queries or did not in docs:
            raise ValueError(f"ID desconhecido no run: {qid}/{did}")
        try:
            rank, score = int(row["rank"]), float(row["score"])
        except (ValueError, TypeError) as exc:
            raise ValueError("rank/score invalidos") from exc
        if rank < 1 or rank > max_rank or not math.isfinite(score):
            raise ValueError(f"rank fora de 1..{max_rank} ou score nao finito")
        runs[qid].append((rank, did, score))
    if len(ids) != 1 or not next(iter(ids)).strip():
        raise ValueError("Cada arquivo deve conter um unico run_id nao vazio")
    result = {}
    for qid, hits in runs.items():
        hits.sort()
        if [x[0] for x in hits] != list(range(1, len(hits) + 1)):
            raise ValueError(f"Ranks duplicados ou nao contiguos: {qid}")
        if len({x[1] for x in hits}) != len(hits):
            raise ValueError(f"Documento duplicado: {qid}")
        if any(hits[i][2] < hits[i + 1][2] for i in range(len(hits) - 1)):
            raise ValueError(f"Score crescente contradiz rank: {qid}")
        result[qid] = [(did, score) for _, did, score in hits]
    return next(iter(ids)), result


def rrf(rankings, k=60, limit=100):
    if k < 1:
        raise ValueError("rrf_k deve ser >=1")
    result = {}
    for qid in sorted(set().union(*(r.keys() for r in rankings))):
        scores = defaultdict(float)
        for system in rankings:
            for rank, (did, _) in enumerate(system.get(qid, []), 1):
                scores[did] += 1 / (k + rank)
        result[qid] = sorted(scores.items(), key=lambda item: (-item[1], item[0]))[:limit]
    return result


def load_qrels(path, docs, queries):
    result = defaultdict(dict)
    for row in read_csv(path):
        if set(row) != {"query_id", "doc_id", "relevance"}:
            raise ValueError("Qrels exigem query_id,doc_id,relevance")
        qid, did = row["query_id"], row["doc_id"]
        rel = float(row["relevance"])
        if qid not in queries or did not in docs or not math.isfinite(rel) or not 0 <= rel <= 10:
            raise ValueError(f"Qrel invalido: {row}")
        if did in result[qid]:
            raise ValueError(f"Qrel duplicado: {qid}/{did}")
        result[qid][did] = rel
    for qid in queries:
        if not any(r > 0 for r in result[qid].values()):
            raise ValueError(f"Consulta sem relevancia positiva no gabarito: {qid}")
    return result


def dcg(relevances):
    return sum((2 ** r - 1) / math.log2(rank + 1) for rank, r in enumerate(relevances, 1))


def evaluate(rankings, queries, qrels, k=10, recall_k=100):
    rows = []
    # Todas as consultas de referencia entram na media, inclusive as ausentes do run.
    for qid in sorted(queries):
        hits = rankings.get(qid, [])
        rels = qrels[qid]
        ideal = dcg(sorted(rels.values(), reverse=True)[:k])
        top = hits[:k]
        relevant = {did for did, rel in rels.items() if rel > 0}
        rows.append({
            "query_id": qid,
            f"ndcg@{k}": dcg([rels.get(did, 0) for did, _ in top]) / ideal if ideal else 0,
            f"mrr@{k}": next((1 / rank for rank, (did, _) in enumerate(top, 1) if rels.get(did, 0) > 0), 0),
            f"recall@{recall_k}": len(relevant & {did for did, _ in hits[:recall_k]}) / len(relevant) if relevant else 0,
            f"judged@{k}": sum(did in rels for did, _ in top) / k,
            "returned": len(hits),
            "missing_query": int(not hits),
        })
    metrics = [f"ndcg@{k}", f"mrr@{k}", f"recall@{recall_k}", f"judged@{k}"]
    summary = {name: sum(row[name] for row in rows) / len(rows) for name in metrics}
    summary.update(queries=len(rows), missing_queries=sum(r["missing_query"] for r in rows))
    return rows, summary
