"""Excel, revisao cruzada e congelamento da avaliacao. Python 3.11+."""
from __future__ import annotations

import hashlib
import json
import math
import re
from collections import defaultdict
from pathlib import Path

from ri_core import (document_text, load_data, load_qrels, load_run, read_csv,
                     read_jsonl, sha256, stable_key, write_csv, write_json, write_jsonl)

ROOT = Path(__file__).resolve().parent
HEADERS = {
    "Dados": ["task_id", "assessor_id", "query_id", "query_text", "doc_id", "title", "text", "relevance", "justificativa"],
    "Adjudicacao": ["task_id", "query_id", "doc_id", "notas", "relevance", "justificativa"],
}


def fresh(folder):
    folder = Path(folder)
    if folder.exists() and any(folder.iterdir()):
        raise ValueError(f"Destino deve estar vazio: {folder}")
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def identifier(value, field):
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", value):
        raise ValueError(f"{field}: use ID textual de 1..64 caracteres A-Z a-z 0-9 _ -")
    return value


def text_value(value, field, optional=False):
    if value is None and optional:
        return ""
    if not isinstance(value, str) or (not optional and not value.strip()):
        raise ValueError(f"Texto ausente/invalido: {field}")
    if len(value) > 32000:
        raise ValueError(f"Texto excede 32000 caracteres: {field}; divida o documento")
    return value.strip()


def grade(value, allow_blank=False):
    if value is None or value == "":
        if allow_blank:
            return None
        raise ValueError("Nota obrigatoria")
    if isinstance(value, bool) or not isinstance(value, (int, float)) or value not in (0, 1, 2):
        raise ValueError("Nota deve ser numero inteiro 0, 1 ou 2")
    return int(value)


def read_sheet(book, name):
    if name not in book.sheetnames:
        raise ValueError(f"Aba ausente: {name}")
    sheet = book[name]
    if list(next(sheet.iter_rows(min_row=1, max_row=1, values_only=True)))[:len(HEADERS[name])] != HEADERS[name]:
        raise ValueError(f"Cabecalho alterado: {name}")
    result = []
    for cells in sheet.iter_rows(min_row=2):
        if not any(c.value is not None for c in cells):
            continue
        if any(c.data_type in ("f", "e") for c in cells):
            raise ValueError(f"Formula/erro proibido na entrada: {name}, linha {cells[0].row}")
        if any(c.value is not None for c in cells[len(HEADERS[name]):]):
            raise ValueError(f"Coluna extra preenchida: {name}")
        result.append(dict(zip(HEADERS[name], [c.value for c in cells])))
    return result


def make_pool(data, runs, proposals, out, depth=10, seed="pool-v2"):
    docs, queries = load_data(data)
    if depth < 1 or depth > 100 or not runs:
        raise ValueError("Pool exige runs e depth entre 1 e 100")
    pairs = set()
    for path in runs:
        _, ranking = load_run(path, docs, queries)
        for qid, hits in ranking.items():
            pairs.update((qid, did) for did, _ in hits[:depth])
    for p in read_csv(proposals):
        if p["query_id"] not in queries or p["doc_id"] not in docs:
            raise ValueError("Referencia desconhecida nas propostas")
        pairs.add((p["query_id"], p["doc_id"]))
    rows = []
    for qid, did in sorted(pairs, key=lambda p: stable_key(seed, ":".join(p))):
        q, d = queries[qid], docs[did]
        rows.append(dict(task_id=hashlib.sha256(f"{qid}\0{did}".encode()).hexdigest()[:24],
                         query_id=qid, query_text=q["text"], doc_id=did,
                         title=d.get("title", ""), text=d["text"],
                         excluded_teams=sorted(set([q.get("origin_team", "")] + d.get("origin_teams", [])) - {""})))
    if {r["query_id"] for r in rows} != set(queries):
        raise ValueError("Pool nao cobre todas as consultas")
    write_jsonl(out, rows)
    write_json(str(out) + ".meta.json", {"pool_sha256": sha256(out),
        "corpus_sha256": sha256(Path(data) / "corpus.jsonl"),
        "queries_sha256": sha256(Path(data) / "queries.jsonl")})
    return rows


def verify_pool(pool, data):
    meta = json.loads(Path(str(pool) + ".meta.json").read_text(encoding="utf-8"))
    expected = {"pool_sha256": sha256(pool), "corpus_sha256": sha256(Path(data) / "corpus.jsonl"),
                "queries_sha256": sha256(Path(data) / "queries.jsonl")}
    if meta != expected:
        raise ValueError("Pool ou dataset alterado; gere novamente os julgamentos")


def assign_pool(pool, data, teams, out, min_assessors=2):
    verify_pool(pool, data)
    docs, queries = load_data(data)
    teams = sorted(set(identifier(t, "team_id") for t in teams))
    if min_assessors < 2:
        raise ValueError("Minimo de dois avaliadores independentes")
    rows = read_jsonl(pool)
    assignments = {team: [] for team in teams}
    for row in rows:
        if row["query_id"] not in queries or row["doc_id"] not in docs:
            raise ValueError("Pool com referencia desconhecida")
        excluded = sorted(set([queries[row["query_id"]].get("origin_team", "")] +
                              docs[row["doc_id"]].get("origin_teams", [])) - {""})
        if row["excluded_teams"] != excluded:
            raise ValueError("Autores excluidos nao correspondem ao dataset")
        eligible = [t for t in teams if t not in row["excluded_teams"]]
        if len(eligible) < min_assessors:
            raise ValueError("Equipes independentes insuficientes; inclua avaliadores da organizacao")
        eligible.sort(key=lambda t: (len(assignments[t]), stable_key(row["task_id"], t)))
        for team in eligible[:min_assessors]:
            assignments[team].append({k: row[k] for k in ("task_id", "query_id", "query_text", "doc_id", "title", "text")})
    target = fresh(out)
    for team, tasks in assignments.items():
        if tasks:
            write_json(target / f"{team}.json", {"assessor_id": team, "tasks": tasks})
    return {t: len(v) for t, v in assignments.items()}


def populate_template(template, out, sheets):
    """Preenche apenas os dados de um template existente para operacao do laboratorio."""
    from copy import copy
    from openpyxl import load_workbook
    out = Path(out)
    if out.exists():
        raise ValueError(f"Arquivo existente: {out}")
    book = load_workbook(template)
    try:
        for name, rows in sheets.items():
            sheet = book[name]
            for row_idx, row in enumerate(rows, 2):
                for col_idx, key in enumerate(HEADERS[name], 1):
                    value = row.get(key)
                    cell = sheet.cell(row_idx, col_idx)
                    if row_idx > 2:
                        cell._style = copy(sheet.cell(2, col_idx)._style)
                    cell.value = value
                    if isinstance(value, str):
                        # Textos da web que comecam com '=' continuam texto, nunca formulas.
                        cell.data_type = "s"
                        cell.number_format = "@"
                # Excel limita altura de linha a 409 pontos. O valor integral permanece na celula.
                lines = max([1] + [math.ceil(len(str(row.get(k) or "")) / width)
                    for k, width in (("text", 75), ("query_text", 45), ("justificativa", 50))])
                sheet.row_dimensions[row_idx].height = min(409, max(25, 16 * lines + 8))
        out.parent.mkdir(parents=True, exist_ok=True)
        book.save(out)
    finally:
        book.close()
    return out


def export_annotation(assignment, outxlsx):
    assignment = json.loads(Path(assignment).read_text(encoding="utf-8"))
    rows = [dict(t, assessor_id=assignment["assessor_id"], relevance=None, justificativa=None)
            for t in assignment["tasks"]]
    return populate_template(ROOT / "templates/avaliacao.xlsx", outxlsx, {"Dados": rows})


def collect_annotations(assignment_dir, workbooks, out):
    from openpyxl import load_workbook
    assignments = {}
    for path in Path(assignment_dir).glob("*.json"):
        a = json.loads(path.read_text(encoding="utf-8"))
        assessor = a["assessor_id"]
        if assessor in assignments:
            raise ValueError("Avaliador repetido no registro")
        assignments[assessor] = {t["task_id"]: t for t in a["tasks"]}
    votes, seen, pending = [], set(), []
    for path in workbooks:
        book = load_workbook(path, data_only=False)
        try:
            for row in read_sheet(book, "Dados"):
                assessor, task = row["assessor_id"], row["task_id"]
                if assessor not in assignments or task not in assignments[assessor] or (assessor, task) in seen:
                    raise ValueError("Voto duplicado ou tarefa nao atribuida ao avaliador")
                seen.add((assessor, task))
                expected = assignments[assessor][task]
                for field in ("query_id", "query_text", "doc_id", "title", "text"):
                    if (row[field] or "") != (expected[field] or ""):
                        raise ValueError(f"Conteudo/ID da tarefa alterado: {task}/{field}")
                rel = grade(row["relevance"], allow_blank=True)
                if rel is None:
                    pending.append({"assessor_id": assessor, "task_id": task})
                    continue
                votes.append(dict(task_id=task, assessor_id=assessor, query_id=row["query_id"],
                                  doc_id=row["doc_id"], relevance=rel,
                                  justificativa=text_value(row["justificativa"], "justificativa")))
        finally:
            book.close()
    for assessor, tasks in assignments.items():
        pending.extend({"assessor_id": assessor, "task_id": t} for t in tasks if (assessor, t) not in seen)
    write_csv(out, ["task_id", "assessor_id", "query_id", "doc_id", "relevance", "justificativa"], votes)
    write_json(str(out) + ".pending.json", pending)
    return {"votes": len(votes), "pending": len(pending)}


def adjudication_rows(pool, votes, min_assessors=2):
    rows = read_jsonl(pool)
    vote_map = defaultdict(list)
    task_map = {r["task_id"]: r for r in rows}
    if len(task_map) != len(rows):
        raise ValueError("task_id duplicado no pool")
    seen = set()
    for v in read_csv(votes):
        task = task_map.get(v["task_id"])
        if task is None or (v["query_id"], v["doc_id"]) != (task["query_id"], task["doc_id"]):
            raise ValueError("Voto fora do pool/referencia alterada")
        key = v["task_id"], v["assessor_id"]
        if key in seen or v["assessor_id"] in task["excluded_teams"]:
            raise ValueError("Voto duplicado ou autor avaliando proprio caso")
        seen.add(key)
        val = float(v["relevance"])
        if val not in (0, 1, 2) or not math.isfinite(val):
            raise ValueError("Nota invalida")
        vote_map[v["task_id"]].append(val)
    issues = []
    for r in rows:
        vals = vote_map[r["task_id"]]
        if len(vals) < min_assessors or len(set(vals)) > 1:
            issues.append(dict(task_id=r["task_id"], query_id=r["query_id"], doc_id=r["doc_id"],
                               notas=",".join(map(str, vals)), relevance=None, justificativa=None))
    return issues, vote_map


def export_adjudication(pool, votes, out, min_assessors=2):
    issues, _ = adjudication_rows(pool, votes, min_assessors)
    populate_template(ROOT / "templates/adjudicacao.xlsx", out, {"Adjudicacao": issues})
    return len(issues)


def finalize_qrels(data, pool, votes, adjudication, out, min_assessors=2):
    from openpyxl import load_workbook
    if min_assessors < 2:
        raise ValueError("Minimo dois avaliadores")
    docs, queries = load_data(data)
    verify_pool(pool, data)
    issues, vote_map = adjudication_rows(pool, votes, min_assessors)
    required = {r["task_id"]: r for r in issues}
    fixes = {}
    if adjudication:
        book = load_workbook(adjudication, data_only=False)
        try:
            for row in read_sheet(book, "Adjudicacao"):
                tid = row["task_id"]
                if tid not in required or tid in fixes:
                    raise ValueError("Adjudicacao duplicada ou nao solicitada")
                if (row["query_id"], row["doc_id"]) != (required[tid]["query_id"], required[tid]["doc_id"]):
                    raise ValueError("IDs alterados na adjudicacao")
                # Falta de votos nao pode ser substituida apenas por uma decisao do organizador.
                if len(vote_map[tid]) < min_assessors:
                    raise ValueError("Complete os votos independentes antes da adjudicacao")
                fixes[tid] = grade(row["relevance"])
                text_value(row["justificativa"], "justificativa de adjudicacao")
        finally:
            book.close()
    if set(fixes) != set(required):
        raise ValueError(f"Pendencias de julgamento/adjudicacao: {len(set(required)-set(fixes))}")
    rows, audit = [], []
    for r in read_jsonl(pool):
        tid = r["task_id"]
        if r["query_id"] not in queries or r["doc_id"] not in docs:
            raise ValueError("Pool com IDs fora do corpus/consultas")
        vals = vote_map[tid]
        rel = fixes.get(tid, vals[0] if vals else None)
        rows.append({"query_id": r["query_id"], "doc_id": r["doc_id"], "relevance": rel})
        audit.append(dict(task_id=tid, votes=len(vals), grades=vals, relevance=rel, adjudicated=tid in fixes))
    # Valida tudo antes de gravar o gabarito oficial.
    positives = {r["query_id"] for r in rows if r["relevance"] > 0}
    if positives != set(queries):
        raise ValueError("Consulta sem positivo no gabarito final; revise o pool")
    if Path(out).exists():
        raise ValueError("Gabarito ja existe; versione em outro caminho")
    write_csv(out, ["query_id", "doc_id", "relevance"], rows)
    load_qrels(out, docs, queries)
    write_json(str(out) + ".audit.json", {"pairs": audit, "qrels_sha256": sha256(out),
        "pool_sha256": sha256(pool), "votes_sha256": sha256(votes),
        "adjudication_sha256": sha256(adjudication) if adjudication else None,
        "corpus_sha256": sha256(Path(data) / "corpus.jsonl"),
        "queries_sha256": sha256(Path(data) / "queries.jsonl")})
    return {"judged_pairs": len(rows), "queries": len(queries), "adjudicated": len(fixes)}


def freeze_solution(folder, stage, out):
    folder, out = Path(folder).resolve(), Path(out).resolve()
    if stage not in ("phase1", "phase2") or out.exists() or out.is_relative_to(folder):
        raise ValueError("Stage invalido, manifesto existente ou dentro da solucao")
    config = json.loads((folder / "config.json").read_text(encoding="utf-8"))
    mode = config.get("mode")
    if ((stage == "phase1" and mode != "lexical") or
        (stage == "phase2" and mode not in ("dense", "rrf", "reranked"))):
        raise ValueError("Metodo nao permitido nesta fase")
    if not (folder / "run.py").is_file():
        raise ValueError("Solucao exige run.py")
    files = {}
    for p in sorted(folder.rglob("*")):
        if p.is_symlink():
            raise ValueError("Links nao sao aceitos na solucao")
        if p.is_file() and "__pycache__" not in p.parts:
            files[p.relative_to(folder).as_posix()] = sha256(p)
    result = {"stage": stage, "team_id": identifier(config["team_id"], "team_id"), "mode": mode, "files": files,
              "toolkit": {n: sha256(ROOT / n) for n in ("ri_core.py", "os_retrieval.py", "config.json")}}
    write_json(out, result)
    return result


def verify_solution(folder, manifest):
    folder = Path(folder).resolve()
    m = json.loads(Path(manifest).read_text(encoding="utf-8"))
    actual = {}
    for p in folder.rglob("*"):
        if p.is_symlink():
            raise ValueError("Links proibidos")
        if p.is_file() and "__pycache__" not in p.parts:
            actual[p.relative_to(folder).as_posix()] = sha256(p)
    if actual != m["files"]:
        raise ValueError("Solucao mudou apos congelamento")
    if m.get("toolkit") != {n: sha256(ROOT / n) for n in ("ri_core.py", "os_retrieval.py", "config.json")}:
        raise ValueError("Toolkit mudou apos congelamento")
    return m
