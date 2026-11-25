# Equipe 16 — Fase 1 (busca léxica BM25)

**ID:** equipe_16

**Integrantes:** [preencher]

## Comando de execução (a partir da raiz do pacote, OpenSearch 3.9.0 em 127.0.0.1:9200)

```
python entregas/equipe_16_phase1_solution/run.py --data data/dev --out resultados/check_fase1 --index ri-equipe_16-check-fase1
```

Gera `run.csv` e `run.meta.json` na pasta de `--out` (que deve ser nova/vazia). O índice de `--index` deve começar com `ri-` e não existir. Dependências: apenas `requirements.txt` do pacote (`requirements-extra.txt` vazio).

## Configurações comparadas (dev: 10 mil documentos, 30 consultas, 1 relevante por consulta)

| experimento | analyzer | k1 | b | NDCG@10 | Recall@100 | MRR@10 |
|---|---|---|---|---|---|---|
| std_k12_b075_v1 | standard | 1.2 | 0.75 | 0.7745 | 0.9667 | 0.7575 |
| pt_k12_b075_v1 | portuguese | 1.2 | 0.75 | 0.8513 | 0.9667 | 0.8256 |
| pt_k09_b040_v1 | portuguese | 0.9 | 0.4 | 0.8579 | 0.9667 | 0.8348 |
| pt_k15_b075_v1 | portuguese | 1.5 | 0.75 | 0.8640 | 0.9667 | 0.8426 |
| pt_k12_b050_v1 | portuguese | 1.2 | 0.5 | 0.8471 | 0.9667 | 0.8198 |
| pt_k12_b090_v1 | portuguese | 1.2 | 0.9 | 0.8539 | 0.9667 | 0.8389 |

[preencher: justificativa de cada variação]

## Decisão final

`pt_k12_b075` — analyzer `portuguese`, k1=1.2, b=0.75, consulta `multi_match` em `title`/`text`, top-100.

[preencher: justificativa]

## Dificuldades conhecidas

- O `os_retrieval.py` copiado para a pasta da entrega lê o `config.json` da equipe como configuração padrão e exige `opensearch_version`; incluímos `"opensearch_version": "3.9.0"` no `config.json` para o `run.py` funcionar.
- [preencher]
