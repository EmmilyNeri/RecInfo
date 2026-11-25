# Fase 1: busca léxica no OpenSearch

Use o ID de equipe já atribuído. Aqui, `data/dev` contém 10 mil documentos WebFAQ, 30 consultas públicas e seus qrels de desenvolvimento; eles não são o teste final. Títulos vazios são válidos: `text` é pesquisável e `doc_id` identifica o resultado.

## Faça nesta ordem

1. Extraia o ZIP. Instale Python 3.11/3.12, Docker Compose e `python -m pip install -r requirements.txt`.
2. Execute `docker compose up -d` e `python -m jupyter lab`; abra `notebooks/00_Ambiente.ipynb` para verificar o OpenSearch 3.9.0.
3. Abra `notebooks/01_fase1.ipynb`, configure o ID e execute no mínimo duas configurações, mudando o analyzer ou parâmetros BM25. Use nomes novos de experimento, índice e saída.
4. Compare NDCG@10, Recall@100 e MRR@10. Salve `comparison.csv` com uma linha por configuração e colunas `experiment,analyzer,bm25_k1,bm25_b,ndcg@10,recall@100,mrr@10`.
5. Escolha uma configuração final. O notebook cria a pasta inicial em `entregas/`; complete os arquivos abaixo e teste a execução antes de compactar.

## Entrega: um ZIP por equipe

Nome: `equipe_XX_fase1.zip`. Na raiz: `run.py`, `config.json`, `README_EQUIPE.md`, `requirements-extra.txt` (vazio se não usar extras) e `resultados_dev/comparison.csv`. Inclua módulos próprios importados. O README informa ID, integrantes, configurações comparadas, decisão final e comando de reprodução.

Exemplo a partir da raiz do pacote extraído: `python entregas/equipe_XX_phase1_solution/run.py --data data/dev --out resultados/check_fase1 --index ri-equipe_XX-check-fase1`. O comando precisa criar `run.csv` e `run.meta.json` conforme `docs/CONTRATOS_E_METRICAS.md`. Não envie corpus, ambiente virtual, índice ou modelo. A organização congela esse código antes do teste agregado.

Após o congelamento, um avaliador pode receber uma planilha `avaliacao.xlsx` **já populada**, individualmente. Preencha apenas `relevance` (0/1/2) e `justificativa`, sem alterar IDs ou textos; devolva no canal privado indicado. Ela não integra o ZIP da Fase 1.
