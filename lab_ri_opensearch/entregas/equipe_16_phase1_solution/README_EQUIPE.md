Integrantes:

* Tarcisio Araujo de Oliveira - 123210061
* Emmily Neri Araújo Almeida - 123210718
* Maria Clara Augusta Santos - 123210361
* Danilo Henrique Peixoto de Sales - 123210295

ID: equipe_16

Configurações comparadas: veja `resultados_dev/comparison.csv`.

Configuração final e justificativa:

**Configuração final:** `analyzer = portuguese`, `bm25_k1 = 0.9`, `bm25_b = 0.90`, modo `lexical` (BM25 puro, sem vetores, fusão ou reranking). Resultado no `data/dev` (30 consultas): nDCG@10 = 0,8662, MRR@10 = 0,8556, Recall@100 = 0,9667.

**Como chegamos nela.** Partimos de um baseline (`portuguese`, k1 = 1,2, b = 0,75: nDCG@10 = 0,8513, MRR@10 = 0,8256) e rodamos um grid de 32 configurações: 2 analyzers (`portuguese`, `standard`) × k1 ∈ {0,9; 1,2; 1,6; 2,0} × b ∈ {0,5; 0,75; 0,9; 1,0}. Depois fizemos um ajuste fino com 3 configurações em torno da melhor região: (k1 = 0,7; b = 0,90), (0,8; 0,95) e (0,9; 0,95). Cada mudança isolava um parâmetro para sabermos o que causou a diferença.

**O que observamos.**

1. *O analyzer foi o fator dominante.* Com `portuguese` o nDCG@10 ficou entre 0,82 e 0,87; com `standard`, entre 0,74 e 0,78 (diferença de cerca de 0,09 nas melhores configurações de cada um). Nossa interpretação é que o stemming e a remoção de stopwords do português fazem formas como "imprimir" e "imprimindo" casarem entre consulta e documento, o que o `standard` não faz.
2. *k1 baixo foi melhor.* A média do nDCG@10 diminui conforme k1 aumenta, nos dois analyzers. Interpretamos que, com a saturação mais rápida do tf, o ranking favorece documentos que cobrem mais termos distintos da consulta em vez de repetições de um mesmo termo.
3. *b alto foi melhor com k1 = 0,9.* Para `portuguese`, k1 = 0,9 com b = 0,9 ou 1,0 deu 0,8662. Interpretamos que penalizar mais os documentos longos favorece respostas mais focadas.
4. *Há um platô.* As configurações (0,9; 0,90), (0,9; 0,95), (0,9; 1,00) e (0,8; 0,95) deram resultados idênticos (nDCG@10 = 0,8662; MRR@10 = 0,8556). Descer para k1 = 0,7 piorou (0,8539), o que delimita a região boa.
5. *Descartamos um pico isolado.* (k1 = 1,6; b = 0,75) deu 0,8640, mas as vizinhas (b = 0,5: 0,833; b = 0,9: 0,854; b = 1,0: 0,840) são bem piores, o que indica pouca estabilidade.

**Por que k1 = 0,9 e b = 0,90.** Como várias configurações empataram, escolhemos o centro do platô em vez do valor mais extremo: `b = 0,9` fica entre os vizinhos de mesmo desempenho (0,95 e 1,0) sem ir ao limite `b = 1`, e `k1 = 0,9` fica a uma distância segura de 0,7, onde o resultado caiu. A ideia é que uma configuração no meio de uma região estável tende a generalizar melhor para o corpus de teste do que uma de borda.

**Limitações da avaliação.** O dev tem só 30 consultas, então o ganho sobre o baseline (cerca de +0,015 de nDCG@10) é pequeno e pode ser ruído. O `judged@10` é baixo (cerca de 9%), ou seja, a maior parte dos documentos recuperados não tem julgamento e conta como não relevante, o que pode subestimar as métricas. O Recall@100 foi 0,9667 (29 de 30 consultas) em todas as configurações `portuguese`, então os ajustes mudaram a ordem dentro do top 10, não os documentos recuperados. [COMPLETAR: se você rodar a comparação consulta a consulta do `per_query.csv` entre o baseline e a final, informe aqui em quantas consultas o nDCG melhorou/piorou/ficou igual; se não rodar, apague esta frase.]

Comando de reprodução, a partir da raiz do pacote: `python entregas/equipe_16_phase1_solution/run.py --data data/dev --out resultados/check_fase1 --index ri-equipe_16-check-fase1`

Dificuldades conhecidas:

* O `config.json` gerado pela célula de entrega original não continha `opensearch_version`, e o `os_retrieval.py` usa esse arquivo como `DEFAULTS`. Isso causava `KeyError` ao rodar o `run.py` a partir da pasta da entrega. Resolvemos adicionando `opensearch_version` (3.9.0) ao `config.json` da entrega, sem alterar nenhum módulo; depois disso o `run.py` rodou sem erros.

* Decidir os melhores valores de `k1` e `b`. Várias configurações ficaram muito próximas em nDCG@10 (algumas idênticas), e com apenas 30 consultas no dev uma diferença pequena pode ser ruído, então olhar só a maior nota não bastava. Resolvemos com duas visualizações: um gráfico de pontos do top 10 por nDCG@10, com o baseline como linha de referência, que mostrou quais configurações estavam de fato empatadas no topo; e um heatmap de k1 × b por analyzer, que mostrou onde há uma região estável (k1 = 0,9 com b entre 0,9 e 1,0) e onde há picos isolados, como (k1 = 1,6; b = 0,75). Com isso passamos a escolher o centro de uma região estável em vez da configuração isolada de maior nota.

* Poucas consultas e `judged@10` baixo limitam a confiança nas diferenças pequenas entre configurações (ver acima).