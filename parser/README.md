# Parser

Este é um programa que implementa um analisador sintático para analisar a estrutura gramatical de uma frase em inglês. Ele usa a biblioteca NLTK (Natural Language Toolkit) para realizar a análise.

## Requisitos

    Python 3.x
    NLTK (Natural Language Toolkit)

Certifique-se de ter o Python instalado em seu sistema e a biblioteca NLTK devidamente instalada.

## Instalação

    1. Faça o download do arquivo parser.py.

    2. Instale a biblioteca NLTK executando o seguinte comando no terminal:
    ```
    pip install nltk
    ```
    ou
    ```
    pip install -r requirements.txt
    ```

## Uso

Execute o programa parser.py da seguinte maneira:
    ```
    python parser.py [caminho_do_arquivo]
    ```
    - Se você fornecer o caminho de um arquivo como argumento, o programa lerá a frase do arquivo.

    - Caso contrário, o programa solicitará que você insira uma frase manualmente.

O programa tentará analisar a frase fornecida e exibirá a árvore sintática resultante, juntamente com os fragmentos de frase nominal encontrados.

## Exemplo

### Entrada
    ```
    python parser.py
    ```

### Saída
    ```
    Sentence: Holmes sat.
            S
    _____|___
    NP        VP
    |         |
    N         V
    |         |
    holmes     sat

    Noun Phrase Chunks
    holmes
    ```
### Observações

    - O programa usa uma gramática definida na variável NONTERMINALS para analisar a estrutura da frase.

    - A função preprocess é usada para pré-processar a frase, convertendo-a para letras minúsculas e removendo palavras não alfabéticas.

    - A função np_chunk retorna todos os fragmentos de frase nominal (NP) na árvore da frase.

    - Se a frase fornecida não puder ser analisada corretamente, o programa exibirá uma mensagem informando que não foi possível analisar a frase.

    - Certifique-se de fornecer frases em inglês como entrada para obter resultados corretos.