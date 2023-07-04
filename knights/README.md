# Lógica Simbólica

Este código implementa uma biblioteca de lógica simbólica em Python. A biblioteca fornece uma estrutura para criar e manipular sentenças lógicas, bem como realizar avaliação de modelos.

## Arquivos

- logic.py: Contém a implementação das classes e funções relacionadas à lógica simbólica.
    
- puzzle.py: Aplicações da biblioteca de lógica simbólica para resolver quebra-cabeças lógicos.

## Classes Principais

### Classe Sentence

Essa classe é a classe base para todas as sentenças lógicas e define métodos comuns a todas as subclasses. Os principais métodos são:

- evaluate(model): Avalia a sentença lógica em um determinado modelo.
    
- formula(): Retorna uma representação em string da fórmula lógica.
    
- symbols(): Retorna um conjunto de todos os símbolos presentes na sentença lógica.

### Classe Symbol

Essa classe representa um símbolo lógico. Cada símbolo possui um nome e pode ser avaliado como verdadeiro ou falso em um determinado modelo. Os principais métodos são:

- evaluate(model): Avalia o valor lógico do símbolo em um determinado modelo.
    
- formula(): Retorna a representação em string do símbolo.
    
- symbols(): Retorna um conjunto contendo o próprio símbolo.

### Outras Classes

O código também inclui as seguintes classes de sentenças lógicas:

- Not: Representa uma negação lógica.
    
- And: Representa uma conjunção lógica entre duas ou mais sentenças.
    
- Or: Representa uma disjunção lógica entre duas ou mais sentenças.
    
- Implication: Representa uma implicação lógica.
    
- Biconditional: Representa uma bicondicional lógica.

## Função model_check

A função model_check implementa a verificação de modelos para avaliar se uma base de conhecimento implica em uma determinada consulta. Ela recebe duas sentenças lógicas como parâmetros: a base de conhecimento e a consulta. A função utiliza a técnica de verificação de modelos para determinar se a base de conhecimento implica na consulta.

## Arquivo puzzle.py

Este arquivo demonstra aplicações da biblioteca de lógica simbólica para resolver quebra-cabeças lógicos. Ele define símbolos para os personagens A, B e C, bem como suas possíveis identidades (Knight ou Knave). A partir disso, são definidas bases de conhecimento para diferentes quebra-cabeças e a função main é chamada para resolver cada um deles. Os resultados são impressos no console.

## Uso

Para utilizar a biblioteca de lógica simbólica, importe o arquivo logic.py e crie sentenças lógicas usando as classes fornecidas. Utilize os métodos apropriados para avaliar, obter a representação em string ou obter os símbolos presentes na sentença. Você também pode utilizar a função model_check para verificar se uma base de conhecimento implica em uma determinada consulta.

    python puzzle.py

Clique aqui para acessar a [página do desafio](https://cs50.harvard.edu/ai/2020/projects/1/knights/). 
