---
language:
- ara
- aze
- ben
- bul
- cat
- ces
- dan
- deu
- ell
- eng
- est
- fas
- fin
- fra
- heb
- hin
- hrv
- hun
- ind
- isl
- ita
- jpn
- kat
- kaz
- kor
- lav
- lit
- mar
- msa
- nld
- nor
- pol
- por
- ron
- rus
- slk
- slv
- spa
- sqi
- srp
- swe
- tgl
- tha
- tur
- ukr
- urd
- uzb
- vie
- zho
multilinguality:
- multilingual
task_categories:
- text-retrieval
task_ids:
- document-retrieval
config_names:
- corpus
tags:
- text-retrieval
dataset_info:
  - config_name: ara-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 6293949
        num_examples: 132664
      - name: test
        num_bytes: 474367
        num_examples: 10000
  - config_name: ara-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 162827578
        num_examples: 142664
  - config_name: ara-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 32958434
        num_examples: 132664
      - name: test
        num_bytes: 2500510
        num_examples: 10000
  - config_name: aze-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 195201
        num_examples: 4382
      - name: test
        num_bytes: 21684
        num_examples: 487
  - config_name: aze-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 2248188
        num_examples: 4869
  - config_name: aze-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 456197
        num_examples: 4382
      - name: test
        num_bytes: 50686
        num_examples: 487
  - config_name: ben-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 585486
        num_examples: 12883
      - name: test
        num_bytes: 65099
        num_examples: 1432
  - config_name: ben-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 16433210
        num_examples: 14315
  - config_name: ben-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 3057883
        num_examples: 12883
      - name: test
        num_bytes: 342824
        num_examples: 1432
  - config_name: bul-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 1449284
        num_examples: 31260
      - name: test
        num_bytes: 160994
        num_examples: 3474
  - config_name: bul-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 56395153
        num_examples: 34734
  - config_name: bul-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 8472065
        num_examples: 31260
      - name: test
        num_bytes: 947542
        num_examples: 3474
  - config_name: cat-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 516924
        num_examples: 11424
      - name: test
        num_bytes: 57474
        num_examples: 1270
  - config_name: cat-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 4645805
        num_examples: 12694
  - config_name: cat-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 955707
        num_examples: 11424
      - name: test
        num_bytes: 105959
        num_examples: 1270
  - config_name: ces-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 3038616
        num_examples: 65077
      - name: test
        num_bytes: 337640
        num_examples: 7231
  - config_name: ces-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 33193093
        num_examples: 72308
  - config_name: ces-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 6114234
        num_examples: 65077
      - name: test
        num_bytes: 671592
        num_examples: 7231
  - config_name: dan-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 6050475
        num_examples: 127686
      - name: test
        num_bytes: 473919
        num_examples: 10000
  - config_name: dan-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 49171909
        num_examples: 137686
  - config_name: dan-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 9957312
        num_examples: 127686
      - name: test
        num_bytes: 775965
        num_examples: 10000
  - config_name: deu-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 42959068
        num_examples: 881201
      - name: test
        num_bytes: 487561
        num_examples: 10000
  - config_name: deu-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 377457585
        num_examples: 891201
  - config_name: deu-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 71911852
        num_examples: 881201
      - name: test
        num_bytes: 819131
        num_examples: 10000
  - config_name: ell-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 1609265
        num_examples: 34664
      - name: test
        num_bytes: 178767
        num_examples: 3852
  - config_name: ell-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 69705751
        num_examples: 38516
  - config_name: ell-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 10020290
        num_examples: 34664
      - name: test
        num_bytes: 1103393
        num_examples: 3852
  - config_name: eng-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 266487011
        num_examples: 5268725
      - name: test
        num_bytes: 505744
        num_examples: 10000
  - config_name: eng-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 1772481467
        num_examples: 5278725
  - config_name: eng-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 393277327
        num_examples: 5268725
      - name: test
        num_bytes: 744279
        num_examples: 10000
  - config_name: est-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 525236
        num_examples: 11601
      - name: test
        num_bytes: 58421
        num_examples: 1290
  - config_name: est-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 4383991
        num_examples: 12891
  - config_name: est-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 908937
        num_examples: 11601
      - name: test
        num_bytes: 101909
        num_examples: 1290
  - config_name: fas-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 10417722
        num_examples: 216940
      - name: test
        num_bytes: 480118
        num_examples: 10000
  - config_name: fas-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 240471393
        num_examples: 226940
  - config_name: fas-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 55308380
        num_examples: 216940
      - name: test
        num_bytes: 2559588
        num_examples: 10000
  - config_name: fin-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 3091007
        num_examples: 66192
      - name: test
        num_bytes: 343482
        num_examples: 7355
  - config_name: fin-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 28033422
        num_examples: 73547
  - config_name: fin-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 5314235
        num_examples: 66192
      - name: test
        num_bytes: 589920
        num_examples: 7355
  - config_name: fra-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 27197413
        num_examples: 559505
      - name: test
        num_bytes: 486112
        num_examples: 10000
  - config_name: fra-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 256564231
        num_examples: 569505
  - config_name: fra-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 50838219
        num_examples: 559505
      - name: test
        num_bytes: 912921
        num_examples: 10000
  - config_name: heb-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 1627547
        num_examples: 35055
      - name: test
        num_bytes: 180930
        num_examples: 3896
  - config_name: heb-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 48378739
        num_examples: 38951
  - config_name: heb-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 7572643
        num_examples: 35055
      - name: test
        num_bytes: 829447
        num_examples: 3896
  - config_name: hin-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 4211562
        num_examples: 90031
      - name: test
        num_bytes: 467737
        num_examples: 10000
  - config_name: hin-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 87202578
        num_examples: 100031
  - config_name: hin-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 22108215
        num_examples: 90031
      - name: test
        num_bytes: 2449171
        num_examples: 10000
  - config_name: hrv-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 222556
        num_examples: 4990
      - name: test
        num_bytes: 24749
        num_examples: 555
  - config_name: hrv-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 1888390
        num_examples: 5545
  - config_name: hrv-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 395678
        num_examples: 4990
      - name: test
        num_bytes: 43710
        num_examples: 555
  - config_name: hun-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 1895908
        num_examples: 40764
      - name: test
        num_bytes: 210690
        num_examples: 4530
  - config_name: hun-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 21346090
        num_examples: 45294
  - config_name: hun-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 3894129
        num_examples: 40764
      - name: test
        num_bytes: 432776
        num_examples: 4530
  - config_name: ind-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 4762169
        num_examples: 101315
      - name: test
        num_bytes: 470046
        num_examples: 10000
  - config_name: ind-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 32240964
        num_examples: 111315
  - config_name: ind-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 8003845
        num_examples: 101315
      - name: test
        num_bytes: 787656
        num_examples: 10000
  - config_name: isl-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 191506
        num_examples: 4300
      - name: test
        num_bytes: 21284
        num_examples: 478
  - config_name: isl-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 2182489
        num_examples: 4778
  - config_name: isl-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 478819
        num_examples: 4300
      - name: test
        num_bytes: 53509
        num_examples: 478
  - config_name: ita-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 11928821
        num_examples: 247803
      - name: test
        num_bytes: 481306
        num_examples: 10000
  - config_name: ita-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 96693889
        num_examples: 257803
  - config_name: ita-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 21034519
        num_examples: 247803
      - name: test
        num_bytes: 852818
        num_examples: 10000
  - config_name: jpn-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 14443765
        num_examples: 299157
      - name: test
        num_bytes: 482708
        num_examples: 10000
  - config_name: jpn-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 254914767
        num_examples: 309157
  - config_name: jpn-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 50949827
        num_examples: 299157
      - name: test
        num_bytes: 1696476
        num_examples: 10000
  - config_name: kat-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 95370
        num_examples: 2164
      - name: test
        num_bytes: 10635
        num_examples: 241
  - config_name: kat-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 3179231
        num_examples: 2405
  - config_name: kat-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 569687
        num_examples: 2164
      - name: test
        num_bytes: 62630
        num_examples: 241
  - config_name: kaz-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 119265
        num_examples: 2695
      - name: test
        num_bytes: 13290
        num_examples: 300
  - config_name: kaz-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 4105845
        num_examples: 2995
  - config_name: kaz-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 751913
        num_examples: 2695
      - name: test
        num_bytes: 79977
        num_examples: 300
  - config_name: kor-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 4307545
        num_examples: 92000
      - name: test
        num_bytes: 468235
        num_examples: 10000
  - config_name: kor-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 65463396
        num_examples: 102000
  - config_name: kor-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 13051430
        num_examples: 92000
      - name: test
        num_bytes: 1411285
        num_examples: 10000
  - config_name: lav-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 534897
        num_examples: 11805
      - name: test
        num_bytes: 59382
        num_examples: 1312
  - config_name: lav-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 5523106
        num_examples: 13117
  - config_name: lav-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 1059030
        num_examples: 11805
      - name: test
        num_bytes: 118211
        num_examples: 1312
  - config_name: lit-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 756757
        num_examples: 16526
      - name: test
        num_bytes: 84084
        num_examples: 1837
  - config_name: lit-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 7954027
        num_examples: 18363
  - config_name: lit-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 1382777
        num_examples: 16526
      - name: test
        num_bytes: 154615
        num_examples: 1837
  - config_name: mar-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 297828
        num_examples: 6663
      - name: test
        num_bytes: 33132
        num_examples: 741
  - config_name: mar-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 6451337
        num_examples: 7404
  - config_name: mar-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 1523782
        num_examples: 6663
      - name: test
        num_bytes: 169123
        num_examples: 741
  - config_name: msa-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 258364
        num_examples: 5786
      - name: test
        num_bytes: 28721
        num_examples: 643
  - config_name: msa-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 1374884
        num_examples: 6429
  - config_name: msa-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 474319
        num_examples: 5786
      - name: test
        num_bytes: 53011
        num_examples: 643
  - config_name: nld-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 17456124
        num_examples: 360662
      - name: test
        num_bytes: 484094
        num_examples: 10000
  - config_name: nld-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 134247494
        num_examples: 370662
  - config_name: nld-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 26845652
        num_examples: 360662
      - name: test
        num_bytes: 747128
        num_examples: 10000
  - config_name: nor-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 2654680
        num_examples: 56908
      - name: test
        num_bytes: 295004
        num_examples: 6324
  - config_name: nor-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 21733914
        num_examples: 63232
  - config_name: nor-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 4389740
        num_examples: 56908
      - name: test
        num_bytes: 486333
        num_examples: 6324
  - config_name: pol-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 8732406
        num_examples: 182515
      - name: test
        num_bytes: 478609
        num_examples: 10000
  - config_name: pol-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 83829979
        num_examples: 192515
  - config_name: pol-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 16387616
        num_examples: 182515
      - name: test
        num_bytes: 891561
        num_examples: 10000
  - config_name: por-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 9556659
        num_examples: 199353
      - name: test
        num_bytes: 479418
        num_examples: 10000
  - config_name: por-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 80179713
        num_examples: 209353
  - config_name: por-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 16301318
        num_examples: 199353
      - name: test
        num_bytes: 816501
        num_examples: 10000
  - config_name: ron-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 2513407
        num_examples: 53902
      - name: test
        num_bytes: 279297
        num_examples: 5990
  - config_name: ron-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 23127529
        num_examples: 59892
  - config_name: ron-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 4627425
        num_examples: 53902
      - name: test
        num_bytes: 517922
        num_examples: 5990
  - config_name: rus-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 18281176
        num_examples: 377504
      - name: test
        num_bytes: 484300
        num_examples: 10000
  - config_name: rus-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 612916055
        num_examples: 387504
  - config_name: rus-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 114319660
        num_examples: 377504
      - name: test
        num_bytes: 3036674
        num_examples: 10000
  - config_name: slk-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 1313413
        num_examples: 28369
      - name: test
        num_bytes: 145901
        num_examples: 3153
  - config_name: slk-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 14900601
        num_examples: 31522
  - config_name: slk-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 2851353
        num_examples: 28369
      - name: test
        num_bytes: 318766
        num_examples: 3153
  - config_name: slv-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 663899
        num_examples: 14551
      - name: test
        num_bytes: 73777
        num_examples: 1617
  - config_name: slv-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 6635100
        num_examples: 16168
  - config_name: slv-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 1171004
        num_examples: 14551
      - name: test
        num_bytes: 129922
        num_examples: 1617
  - config_name: spa-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 28919803
        num_examples: 594661
      - name: test
        num_bytes: 486366
        num_examples: 10000
  - config_name: spa-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 240959272
        num_examples: 604661
  - config_name: spa-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 53980948
        num_examples: 594661
      - name: test
        num_bytes: 913713
        num_examples: 10000
  - config_name: sqi-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 82108
        num_examples: 1869
      - name: test
        num_bytes: 9137
        num_examples: 208
  - config_name: sqi-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 974082
        num_examples: 2077
  - config_name: sqi-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 193094
        num_examples: 1869
      - name: test
        num_bytes: 20854
        num_examples: 208
  - config_name: srp-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 233839
        num_examples: 5241
      - name: test
        num_bytes: 26021
        num_examples: 583
  - config_name: srp-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 4871763
        num_examples: 5824
  - config_name: srp-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 967764
        num_examples: 5241
      - name: test
        num_bytes: 107724
        num_examples: 583
  - config_name: swe-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 7079762
        num_examples: 148738
      - name: test
        num_bytes: 476180
        num_examples: 10000
  - config_name: swe-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 59133680
        num_examples: 158738
  - config_name: swe-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 11970053
        num_examples: 148738
      - name: test
        num_bytes: 803251
        num_examples: 10000
  - config_name: tgl-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 147718
        num_examples: 3327
      - name: test
        num_bytes: 16427
        num_examples: 370
  - config_name: tgl-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 1366620
        num_examples: 3697
  - config_name: tgl-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 256177
        num_examples: 3327
      - name: test
        num_bytes: 28075
        num_examples: 370
  - config_name: tha-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 1986170
        num_examples: 42686
      - name: test
        num_bytes: 220773
        num_examples: 4743
  - config_name: tha-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 58286007
        num_examples: 47429
  - config_name: tha-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 10946198
        num_examples: 42686
      - name: test
        num_bytes: 1213165
        num_examples: 4743
  - config_name: tur-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 6400507
        num_examples: 134846
      - name: test
        num_bytes: 474727
        num_examples: 10000
  - config_name: tur-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 57145253
        num_examples: 144846
  - config_name: tur-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 11003660
        num_examples: 134846
      - name: test
        num_bytes: 812383
        num_examples: 10000
  - config_name: ukr-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 2877527
        num_examples: 61650
      - name: test
        num_bytes: 319800
        num_examples: 6851
  - config_name: ukr-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 96739027
        num_examples: 68501
  - config_name: ukr-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 16581271
        num_examples: 61650
      - name: test
        num_bytes: 1832032
        num_examples: 6851
  - config_name: urd-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 110363
        num_examples: 2497
      - name: test
        num_bytes: 12292
        num_examples: 278
  - config_name: urd-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 3157317
        num_examples: 2775
  - config_name: urd-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 487028
        num_examples: 2497
      - name: test
        num_bytes: 53824
        num_examples: 278
  - config_name: uzb-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 49134
        num_examples: 1136
      - name: test
        num_bytes: 5481
        num_examples: 127
  - config_name: uzb-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 397472
        num_examples: 1263
  - config_name: uzb-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 84009
        num_examples: 1136
      - name: test
        num_bytes: 9237
        num_examples: 127
  - config_name: vie-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 5380320
        num_examples: 113972
      - name: test
        num_bytes: 472088
        num_examples: 10000
  - config_name: vie-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 76390471
        num_examples: 123972
  - config_name: vie-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 14776653
        num_examples: 113972
      - name: test
        num_bytes: 1299967
        num_examples: 10000
  - config_name: zho-qrels
    features:
      - name: query-id
        dtype: string
      - name: corpus-id
        dtype: string
      - name: score
        dtype: float64
    splits:
      - name: train
        num_bytes: 5796595
        num_examples: 122491
      - name: test
        num_bytes: 473244
        num_examples: 10000
  - config_name: zho-corpus
    features:
      - name: _id
        dtype: string
      - name: title
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: corpus
        num_bytes: 79790293
        num_examples: 132491
  - config_name: zho-queries
    features:
      - name: _id
        dtype: string
      - name: text
        dtype: string
    splits:
      - name: train
        num_bytes: 14554815
        num_examples: 122491
      - name: test
        num_bytes: 1183199
        num_examples: 10000
configs:
  - config_name: ara-qrels
    data_files:
      - split: train
        path: ara/qrels-train.jsonl
      - split: test
        path: ara/qrels-test.jsonl
  - config_name: ara-corpus
    data_files:
      - split: corpus
        path: ara/corpus.jsonl
  - config_name: ara-queries
    data_files:
      - split: train
        path: ara/queries-train.jsonl
      - split: test
        path: ara/queries-test.jsonl
  - config_name: aze-qrels
    data_files:
      - split: train
        path: aze/qrels-train.jsonl
      - split: test
        path: aze/qrels-test.jsonl
  - config_name: aze-corpus
    data_files:
      - split: corpus
        path: aze/corpus.jsonl
  - config_name: aze-queries
    data_files:
      - split: train
        path: aze/queries-train.jsonl
      - split: test
        path: aze/queries-test.jsonl
  - config_name: ben-qrels
    data_files:
      - split: train
        path: ben/qrels-train.jsonl
      - split: test
        path: ben/qrels-test.jsonl
  - config_name: ben-corpus
    data_files:
      - split: corpus
        path: ben/corpus.jsonl
  - config_name: ben-queries
    data_files:
      - split: train
        path: ben/queries-train.jsonl
      - split: test
        path: ben/queries-test.jsonl
  - config_name: bul-qrels
    data_files:
      - split: train
        path: bul/qrels-train.jsonl
      - split: test
        path: bul/qrels-test.jsonl
  - config_name: bul-corpus
    data_files:
      - split: corpus
        path: bul/corpus.jsonl
  - config_name: bul-queries
    data_files:
      - split: train
        path: bul/queries-train.jsonl
      - split: test
        path: bul/queries-test.jsonl
  - config_name: cat-qrels
    data_files:
      - split: train
        path: cat/qrels-train.jsonl
      - split: test
        path: cat/qrels-test.jsonl
  - config_name: cat-corpus
    data_files:
      - split: corpus
        path: cat/corpus.jsonl
  - config_name: cat-queries
    data_files:
      - split: train
        path: cat/queries-train.jsonl
      - split: test
        path: cat/queries-test.jsonl
  - config_name: ces-qrels
    data_files:
      - split: train
        path: ces/qrels-train.jsonl
      - split: test
        path: ces/qrels-test.jsonl
  - config_name: ces-corpus
    data_files:
      - split: corpus
        path: ces/corpus.jsonl
  - config_name: ces-queries
    data_files:
      - split: train
        path: ces/queries-train.jsonl
      - split: test
        path: ces/queries-test.jsonl
  - config_name: dan-qrels
    data_files:
      - split: train
        path: dan/qrels-train.jsonl
      - split: test
        path: dan/qrels-test.jsonl
  - config_name: dan-corpus
    data_files:
      - split: corpus
        path: dan/corpus.jsonl
  - config_name: dan-queries
    data_files:
      - split: train
        path: dan/queries-train.jsonl
      - split: test
        path: dan/queries-test.jsonl
  - config_name: deu-qrels
    data_files:
      - split: train
        path: deu/qrels-train.jsonl
      - split: test
        path: deu/qrels-test.jsonl
  - config_name: deu-corpus
    data_files:
      - split: corpus
        path: deu/corpus.jsonl
  - config_name: deu-queries
    data_files:
      - split: train
        path: deu/queries-train.jsonl
      - split: test
        path: deu/queries-test.jsonl
  - config_name: ell-qrels
    data_files:
      - split: train
        path: ell/qrels-train.jsonl
      - split: test
        path: ell/qrels-test.jsonl
  - config_name: ell-corpus
    data_files:
      - split: corpus
        path: ell/corpus.jsonl
  - config_name: ell-queries
    data_files:
      - split: train
        path: ell/queries-train.jsonl
      - split: test
        path: ell/queries-test.jsonl
  - config_name: eng-qrels
    data_files:
      - split: train
        path: eng/qrels-train.jsonl
      - split: test
        path: eng/qrels-test.jsonl
  - config_name: eng-corpus
    data_files:
      - split: corpus
        path: eng/corpus.jsonl
  - config_name: eng-queries
    data_files:
      - split: train
        path: eng/queries-train.jsonl
      - split: test
        path: eng/queries-test.jsonl
  - config_name: est-qrels
    data_files:
      - split: train
        path: est/qrels-train.jsonl
      - split: test
        path: est/qrels-test.jsonl
  - config_name: est-corpus
    data_files:
      - split: corpus
        path: est/corpus.jsonl
  - config_name: est-queries
    data_files:
      - split: train
        path: est/queries-train.jsonl
      - split: test
        path: est/queries-test.jsonl
  - config_name: fas-qrels
    data_files:
      - split: train
        path: fas/qrels-train.jsonl
      - split: test
        path: fas/qrels-test.jsonl
  - config_name: fas-corpus
    data_files:
      - split: corpus
        path: fas/corpus.jsonl
  - config_name: fas-queries
    data_files:
      - split: train
        path: fas/queries-train.jsonl
      - split: test
        path: fas/queries-test.jsonl
  - config_name: fin-qrels
    data_files:
      - split: train
        path: fin/qrels-train.jsonl
      - split: test
        path: fin/qrels-test.jsonl
  - config_name: fin-corpus
    data_files:
      - split: corpus
        path: fin/corpus.jsonl
  - config_name: fin-queries
    data_files:
      - split: train
        path: fin/queries-train.jsonl
      - split: test
        path: fin/queries-test.jsonl
  - config_name: fra-qrels
    data_files:
      - split: train
        path: fra/qrels-train.jsonl
      - split: test
        path: fra/qrels-test.jsonl
  - config_name: fra-corpus
    data_files:
      - split: corpus
        path: fra/corpus.jsonl
  - config_name: fra-queries
    data_files:
      - split: train
        path: fra/queries-train.jsonl
      - split: test
        path: fra/queries-test.jsonl
  - config_name: heb-qrels
    data_files:
      - split: train
        path: heb/qrels-train.jsonl
      - split: test
        path: heb/qrels-test.jsonl
  - config_name: heb-corpus
    data_files:
      - split: corpus
        path: heb/corpus.jsonl
  - config_name: heb-queries
    data_files:
      - split: train
        path: heb/queries-train.jsonl
      - split: test
        path: heb/queries-test.jsonl
  - config_name: hin-qrels
    data_files:
      - split: train
        path: hin/qrels-train.jsonl
      - split: test
        path: hin/qrels-test.jsonl
  - config_name: hin-corpus
    data_files:
      - split: corpus
        path: hin/corpus.jsonl
  - config_name: hin-queries
    data_files:
      - split: train
        path: hin/queries-train.jsonl
      - split: test
        path: hin/queries-test.jsonl
  - config_name: hrv-qrels
    data_files:
      - split: train
        path: hrv/qrels-train.jsonl
      - split: test
        path: hrv/qrels-test.jsonl
  - config_name: hrv-corpus
    data_files:
      - split: corpus
        path: hrv/corpus.jsonl
  - config_name: hrv-queries
    data_files:
      - split: train
        path: hrv/queries-train.jsonl
      - split: test
        path: hrv/queries-test.jsonl
  - config_name: hun-qrels
    data_files:
      - split: train
        path: hun/qrels-train.jsonl
      - split: test
        path: hun/qrels-test.jsonl
  - config_name: hun-corpus
    data_files:
      - split: corpus
        path: hun/corpus.jsonl
  - config_name: hun-queries
    data_files:
      - split: train
        path: hun/queries-train.jsonl
      - split: test
        path: hun/queries-test.jsonl
  - config_name: ind-qrels
    data_files:
      - split: train
        path: ind/qrels-train.jsonl
      - split: test
        path: ind/qrels-test.jsonl
  - config_name: ind-corpus
    data_files:
      - split: corpus
        path: ind/corpus.jsonl
  - config_name: ind-queries
    data_files:
      - split: train
        path: ind/queries-train.jsonl
      - split: test
        path: ind/queries-test.jsonl
  - config_name: isl-qrels
    data_files:
      - split: train
        path: isl/qrels-train.jsonl
      - split: test
        path: isl/qrels-test.jsonl
  - config_name: isl-corpus
    data_files:
      - split: corpus
        path: isl/corpus.jsonl
  - config_name: isl-queries
    data_files:
      - split: train
        path: isl/queries-train.jsonl
      - split: test
        path: isl/queries-test.jsonl
  - config_name: ita-qrels
    data_files:
      - split: train
        path: ita/qrels-train.jsonl
      - split: test
        path: ita/qrels-test.jsonl
  - config_name: ita-corpus
    data_files:
      - split: corpus
        path: ita/corpus.jsonl
  - config_name: ita-queries
    data_files:
      - split: train
        path: ita/queries-train.jsonl
      - split: test
        path: ita/queries-test.jsonl
  - config_name: jpn-qrels
    data_files:
      - split: train
        path: jpn/qrels-train.jsonl
      - split: test
        path: jpn/qrels-test.jsonl
  - config_name: jpn-corpus
    data_files:
      - split: corpus
        path: jpn/corpus.jsonl
  - config_name: jpn-queries
    data_files:
      - split: train
        path: jpn/queries-train.jsonl
      - split: test
        path: jpn/queries-test.jsonl
  - config_name: kat-qrels
    data_files:
      - split: train
        path: kat/qrels-train.jsonl
      - split: test
        path: kat/qrels-test.jsonl
  - config_name: kat-corpus
    data_files:
      - split: corpus
        path: kat/corpus.jsonl
  - config_name: kat-queries
    data_files:
      - split: train
        path: kat/queries-train.jsonl
      - split: test
        path: kat/queries-test.jsonl
  - config_name: kaz-qrels
    data_files:
      - split: train
        path: kaz/qrels-train.jsonl
      - split: test
        path: kaz/qrels-test.jsonl
  - config_name: kaz-corpus
    data_files:
      - split: corpus
        path: kaz/corpus.jsonl
  - config_name: kaz-queries
    data_files:
      - split: train
        path: kaz/queries-train.jsonl
      - split: test
        path: kaz/queries-test.jsonl
  - config_name: kor-qrels
    data_files:
      - split: train
        path: kor/qrels-train.jsonl
      - split: test
        path: kor/qrels-test.jsonl
  - config_name: kor-corpus
    data_files:
      - split: corpus
        path: kor/corpus.jsonl
  - config_name: kor-queries
    data_files:
      - split: train
        path: kor/queries-train.jsonl
      - split: test
        path: kor/queries-test.jsonl
  - config_name: lav-qrels
    data_files:
      - split: train
        path: lav/qrels-train.jsonl
      - split: test
        path: lav/qrels-test.jsonl
  - config_name: lav-corpus
    data_files:
      - split: corpus
        path: lav/corpus.jsonl
  - config_name: lav-queries
    data_files:
      - split: train
        path: lav/queries-train.jsonl
      - split: test
        path: lav/queries-test.jsonl
  - config_name: lit-qrels
    data_files:
      - split: train
        path: lit/qrels-train.jsonl
      - split: test
        path: lit/qrels-test.jsonl
  - config_name: lit-corpus
    data_files:
      - split: corpus
        path: lit/corpus.jsonl
  - config_name: lit-queries
    data_files:
      - split: train
        path: lit/queries-train.jsonl
      - split: test
        path: lit/queries-test.jsonl
  - config_name: mar-qrels
    data_files:
      - split: train
        path: mar/qrels-train.jsonl
      - split: test
        path: mar/qrels-test.jsonl
  - config_name: mar-corpus
    data_files:
      - split: corpus
        path: mar/corpus.jsonl
  - config_name: mar-queries
    data_files:
      - split: train
        path: mar/queries-train.jsonl
      - split: test
        path: mar/queries-test.jsonl
  - config_name: msa-qrels
    data_files:
      - split: train
        path: msa/qrels-train.jsonl
      - split: test
        path: msa/qrels-test.jsonl
  - config_name: msa-corpus
    data_files:
      - split: corpus
        path: msa/corpus.jsonl
  - config_name: msa-queries
    data_files:
      - split: train
        path: msa/queries-train.jsonl
      - split: test
        path: msa/queries-test.jsonl
  - config_name: nld-qrels
    data_files:
      - split: train
        path: nld/qrels-train.jsonl
      - split: test
        path: nld/qrels-test.jsonl
  - config_name: nld-corpus
    data_files:
      - split: corpus
        path: nld/corpus.jsonl
  - config_name: nld-queries
    data_files:
      - split: train
        path: nld/queries-train.jsonl
      - split: test
        path: nld/queries-test.jsonl
  - config_name: nor-qrels
    data_files:
      - split: train
        path: nor/qrels-train.jsonl
      - split: test
        path: nor/qrels-test.jsonl
  - config_name: nor-corpus
    data_files:
      - split: corpus
        path: nor/corpus.jsonl
  - config_name: nor-queries
    data_files:
      - split: train
        path: nor/queries-train.jsonl
      - split: test
        path: nor/queries-test.jsonl
  - config_name: pol-qrels
    data_files:
      - split: train
        path: pol/qrels-train.jsonl
      - split: test
        path: pol/qrels-test.jsonl
  - config_name: pol-corpus
    data_files:
      - split: corpus
        path: pol/corpus.jsonl
  - config_name: pol-queries
    data_files:
      - split: train
        path: pol/queries-train.jsonl
      - split: test
        path: pol/queries-test.jsonl
  - config_name: por-qrels
    data_files:
      - split: train
        path: por/qrels-train.jsonl
      - split: test
        path: por/qrels-test.jsonl
  - config_name: por-corpus
    data_files:
      - split: corpus
        path: por/corpus.jsonl
  - config_name: por-queries
    data_files:
      - split: train
        path: por/queries-train.jsonl
      - split: test
        path: por/queries-test.jsonl
  - config_name: ron-qrels
    data_files:
      - split: train
        path: ron/qrels-train.jsonl
      - split: test
        path: ron/qrels-test.jsonl
  - config_name: ron-corpus
    data_files:
      - split: corpus
        path: ron/corpus.jsonl
  - config_name: ron-queries
    data_files:
      - split: train
        path: ron/queries-train.jsonl
      - split: test
        path: ron/queries-test.jsonl
  - config_name: rus-qrels
    data_files:
      - split: train
        path: rus/qrels-train.jsonl
      - split: test
        path: rus/qrels-test.jsonl
  - config_name: rus-corpus
    data_files:
      - split: corpus
        path: rus/corpus.jsonl
  - config_name: rus-queries
    data_files:
      - split: train
        path: rus/queries-train.jsonl
      - split: test
        path: rus/queries-test.jsonl
  - config_name: slk-qrels
    data_files:
      - split: train
        path: slk/qrels-train.jsonl
      - split: test
        path: slk/qrels-test.jsonl
  - config_name: slk-corpus
    data_files:
      - split: corpus
        path: slk/corpus.jsonl
  - config_name: slk-queries
    data_files:
      - split: train
        path: slk/queries-train.jsonl
      - split: test
        path: slk/queries-test.jsonl
  - config_name: slv-qrels
    data_files:
      - split: train
        path: slv/qrels-train.jsonl
      - split: test
        path: slv/qrels-test.jsonl
  - config_name: slv-corpus
    data_files:
      - split: corpus
        path: slv/corpus.jsonl
  - config_name: slv-queries
    data_files:
      - split: train
        path: slv/queries-train.jsonl
      - split: test
        path: slv/queries-test.jsonl
  - config_name: spa-qrels
    data_files:
      - split: train
        path: spa/qrels-train.jsonl
      - split: test
        path: spa/qrels-test.jsonl
  - config_name: spa-corpus
    data_files:
      - split: corpus
        path: spa/corpus.jsonl
  - config_name: spa-queries
    data_files:
      - split: train
        path: spa/queries-train.jsonl
      - split: test
        path: spa/queries-test.jsonl
  - config_name: sqi-qrels
    data_files:
      - split: train
        path: sqi/qrels-train.jsonl
      - split: test
        path: sqi/qrels-test.jsonl
  - config_name: sqi-corpus
    data_files:
      - split: corpus
        path: sqi/corpus.jsonl
  - config_name: sqi-queries
    data_files:
      - split: train
        path: sqi/queries-train.jsonl
      - split: test
        path: sqi/queries-test.jsonl
  - config_name: srp-qrels
    data_files:
      - split: train
        path: srp/qrels-train.jsonl
      - split: test
        path: srp/qrels-test.jsonl
  - config_name: srp-corpus
    data_files:
      - split: corpus
        path: srp/corpus.jsonl
  - config_name: srp-queries
    data_files:
      - split: train
        path: srp/queries-train.jsonl
      - split: test
        path: srp/queries-test.jsonl
  - config_name: swe-qrels
    data_files:
      - split: train
        path: swe/qrels-train.jsonl
      - split: test
        path: swe/qrels-test.jsonl
  - config_name: swe-corpus
    data_files:
      - split: corpus
        path: swe/corpus.jsonl
  - config_name: swe-queries
    data_files:
      - split: train
        path: swe/queries-train.jsonl
      - split: test
        path: swe/queries-test.jsonl
  - config_name: tgl-qrels
    data_files:
      - split: train
        path: tgl/qrels-train.jsonl
      - split: test
        path: tgl/qrels-test.jsonl
  - config_name: tgl-corpus
    data_files:
      - split: corpus
        path: tgl/corpus.jsonl
  - config_name: tgl-queries
    data_files:
      - split: train
        path: tgl/queries-train.jsonl
      - split: test
        path: tgl/queries-test.jsonl
  - config_name: tha-qrels
    data_files:
      - split: train
        path: tha/qrels-train.jsonl
      - split: test
        path: tha/qrels-test.jsonl
  - config_name: tha-corpus
    data_files:
      - split: corpus
        path: tha/corpus.jsonl
  - config_name: tha-queries
    data_files:
      - split: train
        path: tha/queries-train.jsonl
      - split: test
        path: tha/queries-test.jsonl
  - config_name: tur-qrels
    data_files:
      - split: train
        path: tur/qrels-train.jsonl
      - split: test
        path: tur/qrels-test.jsonl
  - config_name: tur-corpus
    data_files:
      - split: corpus
        path: tur/corpus.jsonl
  - config_name: tur-queries
    data_files:
      - split: train
        path: tur/queries-train.jsonl
      - split: test
        path: tur/queries-test.jsonl
  - config_name: ukr-qrels
    data_files:
      - split: train
        path: ukr/qrels-train.jsonl
      - split: test
        path: ukr/qrels-test.jsonl
  - config_name: ukr-corpus
    data_files:
      - split: corpus
        path: ukr/corpus.jsonl
  - config_name: ukr-queries
    data_files:
      - split: train
        path: ukr/queries-train.jsonl
      - split: test
        path: ukr/queries-test.jsonl
  - config_name: urd-qrels
    data_files:
      - split: train
        path: urd/qrels-train.jsonl
      - split: test
        path: urd/qrels-test.jsonl
  - config_name: urd-corpus
    data_files:
      - split: corpus
        path: urd/corpus.jsonl
  - config_name: urd-queries
    data_files:
      - split: train
        path: urd/queries-train.jsonl
      - split: test
        path: urd/queries-test.jsonl
  - config_name: uzb-qrels
    data_files:
      - split: train
        path: uzb/qrels-train.jsonl
      - split: test
        path: uzb/qrels-test.jsonl
  - config_name: uzb-corpus
    data_files:
      - split: corpus
        path: uzb/corpus.jsonl
  - config_name: uzb-queries
    data_files:
      - split: train
        path: uzb/queries-train.jsonl
      - split: test
        path: uzb/queries-test.jsonl
  - config_name: vie-qrels
    data_files:
      - split: train
        path: vie/qrels-train.jsonl
      - split: test
        path: vie/qrels-test.jsonl
  - config_name: vie-corpus
    data_files:
      - split: corpus
        path: vie/corpus.jsonl
  - config_name: vie-queries
    data_files:
      - split: train
        path: vie/queries-train.jsonl
      - split: test
        path: vie/queries-test.jsonl
  - config_name: zho-qrels
    data_files:
      - split: train
        path: zho/qrels-train.jsonl
      - split: test
        path: zho/qrels-test.jsonl
  - config_name: zho-corpus
    data_files:
      - split: corpus
        path: zho/corpus.jsonl
  - config_name: zho-queries
    data_files:
      - split: train
        path: zho/queries-train.jsonl
      - split: test
        path: zho/queries-test.jsonl
---
<h1 align="center">WebFAQ Retrieval Dataset</h1>
<h4 align="center">
   <p>
       <a href=#overview>Overview</a> |
       <a href=#details>Details</a>  |
       <a href=#structure>Structure</a>  |
       <a href=#examples>Examples</a> |
       <a href=#considerations>Considerations</a> |
       <a href=#license>License</a> |
       <a href=#citation>Citation</a> |
       <a href=#contact>Contact</a> |
       <a href=#acknowledgement>Acknowledgement</a>
   <p>
</h4>

## Overview

The **WebFAQ Retrieval Dataset** is a carefully **filtered and curated subset** of the broader [WebFAQ Q&A Dataset](https://huggingface.co/datasets/PaDaS-Lab/webfaq).  
It is **purpose-built for Information Retrieval (IR)** tasks, such as **training and evaluating** dense or sparse retrieval models in **multiple languages**.

Each of the **49 largest** languages from the WebFAQ corpus has been **thoroughly cleaned** and **refined** to ensure an unblurred notion of relevance between a query (question) and its corresponding document (answer). In particular, we applied:

- **Deduplication** of near-identical questions,  
- **Semantic consistency checks** for question-answer alignment,  
- **Train/Test splits** for retrieval experiments.

## Details

### Languages

The **WebFAQ Retrieval Dataset** covers **49 languages** from the original WebFAQ corpus, both high-resource as well as low-resource. To ensure diversity, the 49 subsets originate from at least 100 different websites each. A single language comprises a few thousands to a few million of QA pairs after our rigorous filtering steps:

#### Top 20 Languages

| Language | # QA pairs |
|----------|-----------:|
| ara      | 143k       |
| dan      | 138k       |
| deu      | 891k       |
| eng      | 5.28M      |
| fas      | 227k       |
| fra      | 570k       |
| hin      | 100k       |
| ind      | 111k       |
| ita      | 258k       |
| jpn      | 309k       |
| kor      | 102k       |
| nld      | 371k       |
| pol      | 193k       |
| por      | 209k       |
| rus      | 388k       |
| spa      | 605k       |
| swe      | 159k       |
| tur      | 145k       |
| vie      | 124k       |
| zho      | 132k       |

<details>
  <summary>  Table of all 49 languages (lexicographical order) </summary>

| Language | # QA pairs | # Test |
|----------|-----------:|-------:|
| ara      |       143k |    10k |
| aze      |       4869 |    487 |
| ben      |      14.3k |   1432 |
| bul      |      34.7k |   3474 |
| cat      |      12.7k |   1270 |
| ces      |      72.3k |   7231 |
| dan      |       138k |    10k |
| deu      |       891k |    10k |
| ell      |      38.5k |   3852 |
| eng      |      5.28M |    10k |
| est      |      12.9k |   1290 |
| fas      |       227k |    10k |
| fin      |      73.5k |   7355 |
| fra      |       570k |    10k |
| heb      |      39.0k |   3896 |
| hin      |       100k |    10k |
| hrv      |       5545 |    555 |
| hun      |      45.3k |   4530 |
| ind      |       111k |    10k |
| isl      |       4778 |    478 |
| ita      |       258k |    10k |
| jpn      |       309k |    10k |
| kat      |       2405 |    241 |
| kaz      |       2995 |    300 |
| kor      |       102k |    10k |
| lav      |      13.1k |   1312 |
| lit      |      18.4k |   1837 |
| mar      |       7404 |    741 |
| msa      |       6429 |    643 |
| nld      |       371k |    10k |
| nor      |      63.2k |   6324 |
| pol      |       193k |    10k |
| por      |       209k |    10k |
| ron      |      59.9k |   5990 |
| rus      |       388k |    10k |
| slk      |      31.5k |   3153 |
| slv      |      16.2k |   1617 |
| spa      |       605k |    10k |
| sqi      |       2077 |    208 |
| srp      |       5824 |    583 |
| swe      |       159k |    10k |
| tgl      |       3697 |    370 |
| tha      |      47.4k |   4743 |
| tur      |       145k |    10k |
| ukr      |      68.5k |   6851 |
| urd      |       2775 |    278 |
| uzb      |       1263 |    127 |
| vie      |       124k |    10k |
| zho      |       132k |    10k |

</details>

<details>
  <summary>  Table of all 49 languages (ordered by size) </summary>

| Language | # QA pairs | # Test |
|----------|-----------:|-------:|
| eng      |      5.28M |    10k |
| deu      |       891k |    10k |
| spa      |       605k |    10k |
| fra      |       570k |    10k |
| rus      |       388k |    10k |
| nld      |       371k |    10k |
| jpn      |       309k |    10k |
| ita      |       258k |    10k |
| fas      |       227k |    10k |
| por      |       209k |    10k |
| pol      |       193k |    10k |
| swe      |       159k |    10k |
| tur      |       145k |    10k |
| ara      |       143k |    10k |
| dan      |       138k |    10k |
| zho      |       132k |    10k |
| vie      |       124k |    10k |
| ind      |       111k |    10k |
| kor      |       102k |    10k |
| hin      |       100k |    10k |
| fin      |      73.5k |   7355 |
| ces      |      72.3k |   7231 |
| ukr      |      68.5k |   6851 |
| nor      |      63.2k |   6324 |
| ron      |      59.9k |   5990 |
| tha      |      47.4k |   4743 |
| hun      |      45.3k |   4530 |
| heb      |      39.0k |   3896 |
| ell      |      38.5k |   3852 |
| bul      |      34.7k |   3474 |
| slk      |      31.5k |   3153 |
| lit      |      18.4k |   1837 |
| slv      |      16.2k |   1617 |
| ben      |      14.3k |   1432 |
| lav      |      13.1k |   1312 |
| est      |      12.9k |   1290 |
| cat      |      12.7k |   1270 |
| mar      |       7404 |    741 |
| msa      |       6429 |    643 |
| srp      |       5824 |    583 |
| hrv      |       5545 |    555 |
| aze      |       4869 |    487 |
| isl      |       4778 |    478 |
| tgl      |       3697 |    370 |
| kaz      |       2995 |    300 |
| urd      |       2775 |    278 |
| kat      |       2405 |    241 |
| sqi      |       2077 |    208 |
| uzb      |       1263 |    127 |

</details>

<details>
  <summary>  NDCG@10 in % for three examplary multilingual embedding models </summary>

| Embedding_Model | #_Params |  ara  |  aze  |  ben  |  bul  |  cat  |  ces  |  dan  |  deu  |  ell  |  eng  |  est  |  fas  |  fin  |  fra  |  heb  |  hin  |  hrv  |  hun  |  ind  |  isl  |  ita  |  jpn  |  kat  |  kaz  |  kor  |  lav  |  lit  |  mar  |  msa  |  nld  |  nor  |  pol  |  por  |  ron  |  rus  |  slk  |  slv  |  spa  |  sqi  |  srp  |  swe  |  tgl  |  tha  |  tur  |  ukr  |  urd  |  uzb  |  vie  |  zho  |
|:----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| [p-m-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) | 118M | 40.89 | 37.90 | 12.82 | 53.62 | 71.06 | 51.63 | 59.31 | 36.34 | 58.14 | 46.86 | 59.81 | 36.30 | 48.04 | 40.35 | 47.71 | 49.73 | 74.91 | 55.53 | 57.92 | 43.15 | 46.64 | 37.43 | 61.09 | 39.35 | 43.36 | 56.48 | 56.04 | 53.56 | 81.57 | 45.85 | 60.91 | 43.59 | 51.48 | 61.22 | 32.97 | 59.42 | 57.91 | 45.17 | 77.38 | 68.31 | 52.39 | 35.78 | 49.84 | 35.96 | 44.77 | 70.47 | 38.61 | 51.42 | 56.43 |
| [m-E5-base](https://huggingface.co/intfloat/multilingual-e5-base) | 278M | 75.66 | 63.51 | 80.90 | 78.65 | 87.34 | 78.66 | 84.14 | 67.91 | 80.34 | 64.29 | 81.33 | 70.01 | 76.14 | 68.66 | 78.82 | 75.26 | 87.22 | 79.47 | 76.65 | 86.22 | 75.52 | 70.02 | 66.22 | 67.90 | 82.52 | 75.78 | 80.28 | 81.16 | 90.75 | 74.60 | 84.46 | 73.67 | 75.61 | 83.08 | 63.21 | 83.62 | 79.27 | 72.72 | 86.77 | 83.17 | 79.03 | 80.79 | 75.24 | 65.02 | 76.17 | 82.17 | 72.52 | 81.93 | 84.18 |
| [jina-v3](https://huggingface.co/jinaai/jina-embeddings-v3) | 572M | 84.64 | 84.31 | 91.85 | 85.25 | 94.74 | 85.99 | 87.53 | 74.22 | 87.01 | 66.70 | 89.72 | 79.49 | 83.52 | 76.41 | 86.80 | 86.86 | 94.67 | 85.44 | 84.02 | 93.11 | 82.29 | 75.29 | 94.49 | 90.17 | 85.41 | 87.00 | 89.65 | 94.46 | 95.10 | 79.85 | 88.59 | 81.27 | 83.13 | 88.43 | 72.02 | 89.34 | 87.33 | 78.63 | 96.36 | 88.85 | 83.68 | 93.60 | 79.23 | 70.96 | 83.88 | 93.27 | 88.91 | 87.40 | 88.85 |

</details>

## Structure

Unlike the raw Q&A dataset, **WebFAQ Retrieval** provides explicit **train/test splits** for each of the 49 languages. The general structure for each language is:

- **Corpus**: A set of unique documents (answers) with IDs and text fields.  
- **Queries**: A set of question strings, each tied to a document ID for relevance.  
- **Qrels**: Relevance labels, mapping each question to its relevant document (corresponding answer).

### Folder Layout (e.g., for eng)

```
eng/
  ├── corpus.jsonl        # all unique documents (answers)
  ├── queries.jsonl       # all queries for train/test
  ├── train.jsonl         # relevance annotations for train
  └── test.jsonl          # relevance annotations for test
```

## Examples

Below is a small snippet showing how to load English train/test sets with [🤗 Datasets](https://github.com/huggingface/datasets):

```python
import json
from datasets import load_dataset
from tqdm import tqdm

# Load train qrels
train_qrels = load_dataset(
    "PaDaS-Lab/webfaq-retrieval",
    "eng-qrels",
    split="train"
)

# Inspect first qrel
print(json.dumps(train_qrels[0], indent=4))

# Load the corpus (answers)
data_corpus = load_dataset(
    "PaDaS-Lab/webfaq-retrieval",
    "eng-corpus",
    split="corpus"
)
corpus = {
    d["_id"]: {"title": d["title"], "text": d["text"]} for d in tqdm(data_corpus)
}

# Inspect first document
print("Document:")
print(json.dumps(corpus[train_qrels[0]["corpus-id"]], indent=4))

# Load all queries
data_queries = load_dataset(
    "PaDaS-Lab/webfaq-retrieval",
    "eng-queries",
    split="queries"
)
queries = {
    q["_id"]: q["text"] for q in tqdm(data_queries)
}

# Inspect first query
print("Query:")
print(json.dumps(queries[train_qrels[0]["query-id"]], indent=4))

# Keep only those queries with relevance annotations
query_ids = set([q["query-id"] for q in train_qrels])
queries = {
    qid: query for qid, query in queries.items() if qid in query_ids
}
print(f"Number of queries: {len(queries)}")
```

Below is a code snippet showing how to evaluate retrieval performance using the `mteb` library:

```python
from mteb import MTEB
from mteb.tasks.Retrieval.multilingual.WebFAQRetrieval import WebFAQRetrieval

# ... Load model ...

# Load the WebFAQ task
task = WebFAQRetrieval()
eval_split = "test"

evaluation = MTEB(tasks=[task])
evaluation.run(
    model,
    eval_splits=[eval_split],
    output_folder="output",
    overwrite_results=True
)
```

## Considerations

Please note the following considerations when using the collected QAs:

- *[Q&A Dataset]* **Risk of Duplicate or Near-Duplicate Content**: The raw Q&A dataset is large and includes minor paraphrases.  
- *[Retrieval Dataset]* **Sparse Relevance**: As raw FAQ data, each question typically has one “best” (on-page) answer. Additional valid answers may exist on other websites but are not labeled as relevant.  
- **Language Detection Limitations**: Some QA pairs mix languages, or contain brand names, which can confuse automatic language classification.  
- **No Guarantee of Factual Accuracy**: Answers reflect the content of the source websites. They may include outdated, biased, or incorrect information.  
- **Copyright and Privacy**: Please ensure compliance with any applicable laws and the source website’s terms.

## License

The **Collection of WebFAQ Datasets** is shared under [**Creative Commons Attribution 4.0 (CC BY 4.0)**](https://creativecommons.org/licenses/by/4.0/) license.

> **Note**: The dataset is derived from public webpages in Common Crawl snapshots (2022–2024) and intended for **research purposes**. Each FAQ’s text is published by the original website under their terms. Downstream users should verify any usage constraints from the **original websites** as well as [Common Crawl’s Terms of Use](https://commoncrawl.org/terms-of-use/).

## Citation

If you use this dataset in your research, please consider citing the associated paper:

```bibtex
@misc{dinzinger2025webfaq,
    title={WebFAQ: A Multilingual Collection of Natural Q&amp;A Datasets for Dense Retrieval},
    author={Michael Dinzinger and Laura Caspari and Kanishka Ghosh Dastidar and Jelena Mitrović and Michael Granitzer},
    year={2025},
    eprint={2502.20936},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

## Contact

For inquiries and feedback, please feel free to contact us via E-Mail ([michael.dinzinger@uni-passau.de](mailto:michael.dinzinger@uni-passau.de)) or start a discussion on HuggingFace or GitHub.

## Acknowledgement

We thank the Common Crawl and Web Data Commons teams for providing the underlying data, and all contributors who helped shape the WebFAQ project.

### Thank you

We hope the **Collection of WebFAQ Datasets** serves as a valuable resource for your research. Please consider citing it in any publications or projects that use it. If you encounter issues or want to contribute improvements, feel free to get in touch with us on HuggingFace or GitHub.

Happy researching!