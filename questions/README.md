# Questions

Este é um programa em Python que permite fazer perguntas sobre um conjunto de documentos de texto usando o algoritmo TF-IDF (Term Frequency-Inverse Document Frequency). O programa identifica os arquivos mais relevantes e as frases mais relevantes que correspondem à consulta fornecida.

## Requisitos

    Python 3.x
    Biblioteca NLTK (Natural Language Toolkit)

Certifique-se de ter o NLTK instalado e também de ter os pacotes de dados necessários, executando o seguinte comando antes de executar o programa:
    ```
    python -m nltk.downloader stopwords
    ```

## Uso

Execute o programa fornecendo o diretório onde estão localizados os documentos de texto como argumento da linha de comando:
    ```
    python questions.py corpus
    ```

Após executar o programa, ele solicitará uma consulta. Insira a consulta desejada e pressione Enter. O programa calculará as correspondências de arquivos mais relevantes com base no TF-IDF e, em seguida, extrairá as frases mais relevantes desses arquivos. As frases serão exibidas na saída.

Exemplo:
    ```
    Query: What are the types of supervised learning?
    Types of supervised learning algorithms include Active learning , classification and regression.
    ```

## Funções Principais

### load_files(directory)
    Esta função recebe um nome de diretório e retorna um dicionário que mapeia o nome de cada arquivo .txt dentro desse diretório para o conteúdo do arquivo como uma string.

### tokenize(document)
    Esta função recebe um documento (representado como uma string) e retorna uma lista de todas as palavras contidas no documento, em ordem. O documento é processado convertendo todas as palavras para minúsculas e removendo pontuação e stopwords em inglês.

### compute_idfs(documents)
    Esta função recebe um dicionário de documents, que mapeia os nomes dos documentos para uma lista de palavras, e retorna um dicionário que mapeia as palavras para seus valores IDF (Inverse Document Frequency). Qualquer palavra que apareça em pelo menos um dos documentos estará no dicionário resultante.

### top_files(query, files, idfs, n)
    Esta função recebe uma query (um conjunto de palavras), files (um dicionário que mapeia nomes de arquivos para uma lista de suas palavras), e idfs (um dicionário que mapeia palavras para seus valores IDF) e retorna uma lista dos nomes dos n arquivos principais que correspondem à consulta, classificados de acordo com o TF-IDF.

### top_sentences(query, sentences, idfs, n)
    Esta função recebe uma query (um conjunto de palavras), sentences (um dicionário que mapeia frases para uma lista de suas palavras) e idfs (um dicionário que mapeia palavras para seus valores IDF) e retorna uma lista das n frases principais que correspondem à consulta, classificadas de acordo com o IDF. Em caso de empate, é dada preferência às frases com uma maior densidade de termos da consulta.