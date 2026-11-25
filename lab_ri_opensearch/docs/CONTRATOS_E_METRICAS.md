# Contratos dos arquivos e métricas

## Dados

Um documento por linha de `corpus.jsonl`:

```json
{"doc_id":"equipe_01__d01","title":"","text":"Conteúdo pesquisável"}
```

Uma consulta por linha de `queries.jsonl`:

```json
{"query_id":"equipe_01__q01","text":"Consulta em linguagem natural","stage":"phase1","origin_team":"equipe_01"}
```

Os metadados `stage`, `origin_team` e `origin_teams` são usados pela organização para separar fases e evitar juízes autores dos pares. O OpenSearch indexa apenas `doc_id`, `title`, `text` e, quando necessário, `embedding`. A entrada de execução de uma solução não recebe os qrels nem as propostas do autor.

O gabarito final tem exatamente estas colunas:

```csv
query_id,doc_id,relevance
equipe_01__q01,equipe_01__d01,2
```

As notas oficiais dos novos casos são inteiros 0, 1 e 2. A relevância 1 dos qrels públicos WebFAQ indica um positivo binário de desenvolvimento; não é uma avaliação humana parcial da turma. São protocolos distintos.

## Ranking

```csv
run_id,query_id,doc_id,rank,score
equipe_01_lexical,equipe_01__q01,equipe_01__d01,1,8.42
```

IDs são strings. Cada arquivo tem um único run_id. Ranks começam em 1, são contíguos e limitados a 100 por consulta. Scores devem ser finitos e não crescentes. Documento repetido para a mesma consulta e IDs desconhecidos são rejeitados. Consultas ausentes contam zero no denominador. Um arquivo inteiro sem nenhum resultado é inválido pelo contrato de submissão; a organização deve registrar a falha da execução.

## Etapas de recuperação

| Método | Entrada | Processamento | Saída |
|---|---|---|---|
| Léxico | Consulta e campos text/title | Multi-match com BM25 no OpenSearch, analyzer configurável | Até 100 documentos |
| Semântico | Consulta e conteúdo textual | E5 com prefixos query/passagem definidos pelo modelo; vetores normalizados, k-NN HNSW/Lucene, similaridade cosseno | Até 100 documentos |
| RRF | Rankings léxico e semântico | Soma de `1 / (rrf_k + rank)`, por documento; padrão rrf_k=60 | Até 100 documentos da união |
| Reranking | Consulta e candidatos RRF | CrossEncoder avalia o par consulta–documento e reordena | Mesmos candidatos, nova ordem |

Os prefixos literais do E5 são `query: ` e `passage: `, mesmo em português. O conteúdo é `title + quebra de linha + text`, removendo bordas vazias. Com título vazio, equivale a text. O CrossEncoder usa texto original e consulta, sem tokenização lexical manual. Scores do CrossEncoder são usados para ordenação, sem interpretação como probabilidades calibradas.

Fusão e reranking estão no cliente Python. O OpenSearch armazena os dados e realiza as duas recuperações. Na avaliação, scores de métodos diferentes não são somados diretamente.

## Avaliação

`DCG@10 = soma((2**relevance - 1) / log2(rank + 1))`, com rank a partir de 1.

`NDCG@10 = DCG@10 / IDCG@10`. O ideal usa os dez maiores julgamentos de todos os qrels da consulta, inclusive documentos não recuperados. O resultado global é a média de todas as consultas esperadas. Consulta sem positivo no gabarito bloqueia a finalização dos qrels.

`Recall@100` considera os relevantes conhecidos nos qrels. `MRR@10` é o inverso da primeira posição com relevância maior que zero, até dez. `Judged@10` é o número de documentos julgados no top 10 dividido por dez.

Documentos não julgados recebem ganho zero por convenção de avaliação. O protocolo não os declara factualmente irrelevantes. O pool deve conter os resultados finais de todos os métodos/equipes e seus baselines antes de ser julgado.

Na Fase 2, `delta_ndcg@10` é a diferença contra o baseline léxico congelado da própria equipe, executado no mesmo corpus e nas mesmas consultas phase2. Os resultados das fases 1 e 2 isoladamente não são uma comparação pareada.
