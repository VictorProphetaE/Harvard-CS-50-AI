# Shopping.py

Este é um programa Python que utiliza o algoritmo K-Nearest Neighbors para classificar dados relacionados a compras online. O programa carrega dados de um arquivo CSV, divide-os em conjuntos de treinamento e teste, treina o modelo e faz previsões. Em seguida, ele avalia a precisão do modelo com base nos rótulos reais e imprime os resultados.

## Requisitos

    Python 3.x
    Biblioteca scikit-learn

Certifique-se de ter a biblioteca scikit-learn instalada antes de executar o programa.

## Uso

Execute o programa a partir da linha de comando, fornecendo o nome do arquivo de dados como argumento:
    ```
    python shopping.py dados.csv
    ```
Certifique-se de substituir dados.csv pelo caminho e nome do seu próprio arquivo de dados.

## Formato dos dados

O arquivo de dados CSV deve ter as seguintes colunas:

    - Administrative: um número inteiro
    - Administrative_Duration: um número de ponto flutuante
    - Informational: um número inteiro
    - Informational_Duration: um número de ponto flutuante
    - ProductRelated: um número inteiro
    - ProductRelated_Duration: um número de ponto flutuante
    - BounceRates: um número de ponto flutuante
    - ExitRates: um número de ponto flutuante
    - PageValues: um número de ponto flutuante
    - SpecialDay: um número de ponto flutuante
    - Month: um índice de 0 (janeiro) a 11 (dezembro)
    - OperatingSystems: um número inteiro
    - Browser: um número inteiro
    - Region: um número inteiro
    - TrafficType: um número inteiro
    - VisitorType: um inteiro 0 (não retornado) ou 1 (retornado)
    - Weekend: um inteiro 0 (se falso) ou 1 (se verdadeiro)
    - Revenue: um inteiro 0 (se falso) ou 1 (se verdadeiro)

Certifique-se de que o arquivo de dados esteja formatado corretamente de acordo com essas especificações.

## Resultados

O programa exibirá os seguintes resultados:

    Quantidade de previsões corretas
    Quantidade de previsões incorretas
    Taxa de verdadeiros positivos (sensibilidade)
    Taxa de verdadeiros negativos (especificidade)

Os resultados serão exibidos no formato a seguir:

    Correct: 4088
    Incorrect: 844
    True Positive Rate: 41.02%
    True Negative Rate: 90.55%

Substitua X, Y, Z e W pelos valores reais calculados pelo programa.

Acesse a [página do desafio](https://cs50.harvard.edu/ai/2020/projects/4/shopping/) para acessar a página do desafio.
