# PageRank

Este é um programa em Python que implementa o algoritmo PageRank. O PageRank é um algoritmo utilizado pelo Google para classificar as páginas da web em ordem de relevância. Ele atribui um valor numérico chamado "PageRank" a cada página com base em sua importância relativa.

## Uso

Certifique-se de ter o Python instalado em seu sistema. Para executar o programa, siga as etapas abaixo:

1. Abra um terminal.

2. Navegue até o diretório onde o arquivo pagerank.py está localizado.

3. Execute o seguinte comando:
   
    ```
    python pagerank.py corpus0
    ```
    
5. Substitua corpus pelo diretório contendo as páginas HTML para as quais você deseja calcular o PageRank.

## Dependências

O programa requer as seguintes dependências:

    Python 3.x

Certifique-se de ter essas dependências instaladas antes de executar o programa.

## Descrição do Arquivo

    pagerank.py: O arquivo principal que contém a implementação do algoritmo PageRank.

## Funcionalidades

- crawl(directory)

Essa função analisa um diretório de páginas HTML e verifica os links para outras páginas. Ela retorna um dicionário em que cada chave é uma página e os valores são uma lista de todas as outras páginas no corpus que estão vinculadas à página.

- transition_model(corpus, page, damping_factor)

Essa função retorna uma distribuição de probabilidade sobre qual página visitar em seguida, dada uma página atual. Com probabilidade damping_factor, escolhe um link aleatório vinculado à page. Com probabilidade 1 - damping_factor, escolhe um link aleatório escolhido entre todas as páginas do corpus.

- sample_pagerank(corpus, damping_factor, n)

Essa função retorna os valores do PageRank para cada página por amostragem de n páginas de acordo com o modelo de transição, começando por uma página aleatória. Ela retorna um dicionário em que as chaves são os nomes das páginas e os valores são seus valores estimados de PageRank (um valor entre 0 e 1). Todos os valores do PageRank devem somar 

- iterate_pagerank(corpus, damping_factor)

Essa função retorna os valores do PageRank para cada página atualizando iterativamente os valores do PageRank até a convergência. Ela retorna um dicionário em que as chaves são os nomes das páginas e os valores são seus valores estimados de PageRank (um valor entre 0 e 1). Todos os valores do PageRank devem somar 1.

## Resultados

O programa exibirá os resultados do PageRank para o corpus fornecido. Ele exibirá os resultados a partir da amostragem e da iteração, mostrando o nome da página e seu valor de PageRank.

Clique aqui para acessar a [página do desafio](https://cs50.harvard.edu/ai/2020/projects/2/pagerank/).  
