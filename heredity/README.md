# heredity.py

Este programa calcula as probabilidades de herança de características genéticas usando uma rede bayesiana. Ele determina as probabilidades de ter genes e características específicas com base em dados fornecidos.

## Forma de Uso

Para executar o programa, use o seguinte comando:

    python heredity.py data/family0.csv

## Dependências

Este programa requer as seguintes dependências:

    - Python 3.x
    - csv module
    - itertools module
    - sys module

Verifique se o Python está instalado em seu sistema e se os módulos necessários estão disponíveis.

## Funcionalidade

O programa executa as seguintes etapas:

1. Carrega dados de genes e características de um arquivo CSV em um dicionário.
    
2. Calcula as probabilidades de ter genes e características para cada pessoa.
    
3. Considera todas as combinações possíveis de pessoas que podem ter uma característica específica.
    
4. Considera todas as combinações possíveis de pessoas que podem ter um número específico de genes.
    
5. Atualiza as probabilidades com base na probabilidade conjunta dos dados fornecidos.
    
6. Normaliza as probabilidades para garantir que somam 1.
    
7. Imprime os resultados, mostrando as probabilidades de genes e características para cada pessoa.

Certifique-se de que seu arquivo de dados CSV segue o formato necessário:

1. O arquivo deve conter os seguintes campos: nome, mãe, pai, característica.
    
2. Os campos mãe e pai devem estar em branco ou nomes válidos no CSV.
    
3. O campo de característica deve conter 0 ou 1 se a característica for conhecida, ou ficar em branco se a característica for desconhecida.

Nota: O programa assume que a probabilidade de mutação é 0,01.

## Exemplo

Suponha que você tenha um arquivo de dados chamado data.csv com o seguinte conteúdo:

    name,mother,father,trait
    Harry,Lily,James,
    James,,,1
    Lily,,,0

A execução do programa com esse arquivo de dados forneceria as probabilidades de genes e características de cada pessoa.

Saída de exemplo:

    Harry:
    Gene:
        2: 0.0092
        1: 0.4557
        0: 0.5351
    Trait:
        True: 0.2665
        False: 0.7335
    James:
    Gene:
        2: 0.1976
        1: 0.5106
        0: 0.2918
    Trait:
        True: 1.0000
        False: 0.0000
    Lily:
    Gene:
        2: 0.0036
        1: 0.0136
        0: 0.9827
    Trait:
        True: 0.0000
        False: 1.0000

Acesse a [página do desafio](https://cs50.harvard.edu/ai/2020/projects/2/heredity/) para acessar a página do desafio. 
