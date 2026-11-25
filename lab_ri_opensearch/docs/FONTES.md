# Fontes verificadas em 28/10/2026

- OpenSearch, versão e histórico: https://docs.opensearch.org/latest/version-history/ . Versão 3.9.0 publicada em 29/09/2026. Fixada para este pacote; atualizar somente antes de congelar as soluções e após homologação.
- Docker oficial: https://docs.opensearch.org/latest/install-and-configure/install-opensearch/docker/ . Imagem fixada `opensearchproject/opensearch:3.9.0`, sem tag latest.
- Vetores: https://docs.opensearch.org/latest/mappings/supported-field-types/knn-vector/ . O adaptador usa `knn_vector`, HNSW/Lucene e `cosinesimil`.
- Busca híbrida: https://docs.opensearch.org/latest/vector-search/ai-search/hybrid-search/index/ . A API nativa é uma alternativa; no pacote entregue RRF é aplicada em Python aos rankings do OpenSearch.
- Reranking: https://docs.opensearch.org/latest/search-plugins/search-relevance/reranking-search-results/ . No pacote entregue o CrossEncoder é executado no cliente.
- WebFAQ: https://huggingface.co/datasets/PaDaS-Lab/webfaq-retrieval . Código dos autores: https://github.com/padas-lab-de/webfaq . Paper: https://arxiv.org/abs/2502.20936 . Revisão original, seed do recorte, IDs públicos e hashes dos arquivos estão em `data/origem_v2.json`; o card original acompanha o pacote.
- E5 multilíngue: https://huggingface.co/intfloat/multilingual-e5-small . Prefixos `query: ` e `passage: `, inclusive em português.
- mMARCO CrossEncoder: https://huggingface.co/cross-encoder/mmarco-mMiniLMv2-L12-H384-v1 . Modelos e revisões em `config.json`.

As decisões de cotas, sigilo operacional, revisão cruzada e separação das fases são regras locais propostas para este laboratório; não são características garantidas pelas bases públicas ou pelo OpenSearch.
