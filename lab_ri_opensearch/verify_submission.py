"""Verifica uma pasta de solução com OpenSearch local já iniciado.

Uso: python verify_submission.py --solution entregas/equipe_XX_phase1_solution
"""
import argparse
import json
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path

from ri_core import load_data, load_run


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--solution", required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    solution = Path(args.solution).resolve()
    required = ["run.py", "config.json", "README_EQUIPE.md", "requirements-extra.txt", "resultados_dev/comparison.csv"]
    config = json.loads((solution / "config.json").read_text(encoding="utf-8"))
    if config.get("mode") != "lexical":
        required.append("strategies.py")
    missing = [name for name in required if not (solution / name).is_file()]
    if missing:
        raise SystemExit(f"Arquivos ausentes: {missing}")
    with tempfile.TemporaryDirectory(prefix="ri-verify-") as tmp:
        out = Path(tmp) / "result"
        index = "ri-verify-" + uuid.uuid4().hex[:12]
        subprocess.run([sys.executable, str(solution / "run.py"), "--data", str(root / "data/dev"),
                        "--out", str(out), "--index", index], check=True)
        docs, queries = load_data(root / "data/dev")
        load_run(out / "run.csv", docs, queries)
        meta = json.loads((out / "run.meta.json").read_text(encoding="utf-8"))
        if meta["config"]["team_id"] != config["team_id"]:
            raise ValueError("team_id divergente no metadata")
        print(f"OK: solução reproduzida; {len(queries)} consultas; índice {index}")


if __name__ == "__main__":
    main()
