# Crossword Generator

Este é um programa em Python que resolve palavras cruzadas usando busca por retrocesso (backtracking). O programa consiste em dois arquivos principais:

- `crossword.py`: Contém as definições das classes `Variable` e `Crossword` relacionadas à representação e estrutura das palavras cruzadas.
- `generate.py`: Contém a implementação da classe `CrosswordCreator`, que utiliza o algoritmo de busca por retrocesso para resolver as palavras cruzadas.

## crossword.py

Este arquivo contém duas classes: Variable e Crossword.

### Variable

A classe Variable representa uma variável de palavras cruzadas, que pode ser uma palavra cruzada ou uma palavra negativa. Cada variável tem um ponto de partida, direção e comprimento. A classe Variable fornece métodos para hashing, comparação de igualdade e representação de string.

### Crossword

A classe Crossword representa o próprio jogo de palavras cruzadas. Ele lê a estrutura das palavras cruzadas de um arquivo de estrutura e a lista de palavras de um arquivo de palavras. Ele determina as variáveis nas palavras cruzadas com base na estrutura e calcula as sobreposições entre as variáveis. A classe Crossword também fornece um método para obter as variáveis vizinhas de uma determinada variável.

## generate.py

Este arquivo contém a classe CrosswordCreator, responsável por gerar as palavras cruzadas.

### CrosswordCreator

A classe CrosswordCreator recebe um objeto Crossword como entrada e executa a geração de palavras cruzadas. Ele usa o algoritmo de retrocesso para encontrar uma atribuição válida de palavras para as variáveis nas palavras cruzadas. A classe fornece métodos para impor consistência de nó, revisar domínios e executar consistência de arco. Ele também possui métodos para verificar a completude e a consistência das atribuições, ordenar os valores do domínio, selecionar variáveis não atribuídas e realizar a pesquisa retroativa.

A função main() neste arquivo é o ponto de entrada do programa. Ele lê a estrutura e os arquivos de palavras dos argumentos da linha de comando, cria um objeto Crossword e usa o CrosswordCreator para resolver e imprimir as palavras cruzadas. Opcionalmente, ele pode salvar as palavras cruzadas geradas em um arquivo de imagem de saída.

## Uso

O programa pode ser executado a partir da linha de comando com os seguintes argumentos:
    ```
    python generate.py structure words [output]
    ```
    - `structure`: O caminho para o arquivo contendo a estrutura das palavras cruzadas.
    - `words`: O caminho para o arquivo contendo a lista de palavras disponíveis para preencher as palavras cruzadas.
    - `output` (opcional): O caminho para o arquivo de saída onde a solução será salva como uma imagem.

Se nenhum arquivo de saída for especificado, a solução será apenas impressa no terminal.

## Formato dos Arquivos

### Arquivo de Estrutura

O arquivo de estrutura especifica a grade das palavras cruzadas. Cada linha do arquivo representa uma linha da grade. Os caracteres `_` representam células vazias onde as letras devem ser preenchidas, e outros caracteres representam células bloqueadas (não podem ser preenchidas). Por exemplo:

#___#
#_##_
#_##_
#_##_
#____

### Arquivo de Palavras

O arquivo de palavras contém uma lista de palavras válidas para preencher as palavras cruzadas. Cada palavra deve estar em uma linha separada. Por exemplo:

one
two
three
four
five
six
seven
eight
nine
ten


## Dependências

O programa requer a biblioteca Python PIL (Pillow) para gerar e salvar a imagem da solução. Você pode instalá-la usando o comando:
    ```
    pip install Pillow
    ```

## Exemplo de Execução
    ```
    python generate.py data/structure1.txt data/words1.txt output.png
    ```

Este comando lê a estrutura das palavras cruzadas do arquivo `structure.txt`, a lista de palavras do arquivo `words.txt`, e salva a solução como uma imagem no arquivo `output.png`.


Note: The program requires the PIL (Python Imaging Library) package to save the crossword as an image. Make sure to install the required dependencies before running the program.
