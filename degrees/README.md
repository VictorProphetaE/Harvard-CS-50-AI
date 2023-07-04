# degrees.py

Este script é usado para calcular o grau de separação entre duas pessoas usando dados de filmes. Ele carrega os dados de arquivos CSV em memória e utiliza o algoritmo de busca em largura para encontrar o caminho mais curto entre as duas pessoas.

## Uso

Certifique-se de ter os arquivos people.csv, movies.csv e stars.csv no diretório especificado ou no diretório padrão large. Execute o script da seguinte maneira:

    python degrees.py large
    Loading data...
    Data loaded.
    
Ao executar o script, você será solicitado a inserir o nome da pessoa de origem e o nome da pessoa de destino. O script encontrará o caminho mais curto entre essas duas pessoas e exibirá o resultado na saída.

    Name: Emma Watson
    Name: Jennifer Lawrence
    3 degrees of separation.
    1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
    2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
    3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class

## Dependências

    Python 3.x
    Biblioteca CSV

Certifique-se de ter o Python instalado no seu sistema e que a biblioteca CSV esteja disponível. Você pode instalá-la usando o pip:

    pip install csv
    
## util.py

Este arquivo contém as classes Node, StackFrontier e QueueFrontier, que são usadas pelo script degrees.py para implementar a busca em largura.

Não são necessários comandos adicionais para executar diretamente o util.py. Ele é importado e usado pelo script degrees.py.

Acesse a [página do desafio](https://cs50.harvard.edu/ai/2020/projects/0/degrees/) para acessar a página do desafio. 
