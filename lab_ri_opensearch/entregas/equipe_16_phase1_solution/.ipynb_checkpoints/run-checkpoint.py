"""Entrada de submissão: python run.py --data ... --out ... --index ..."""
import argparse
import json
from pathlib import Path
from os_retrieval import run_experiment

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--index", required=True)
    args = parser.parse_args()
    config = json.loads(Path(__file__).with_name("config.json").read_text(encoding="utf-8"))
    if config["mode"] == "lexical":
        run_experiment(args.data, args.out, config, args.index)
    else:
        import strategies
        run_experiment(args.data, args.out, config, args.index, strategies=strategies)
