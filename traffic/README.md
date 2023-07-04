# Tráfego - Reconhecimento de Sinais de Trânsito

Este é um programa em Python que realiza o reconhecimento de sinais de trânsito utilizando redes neurais convolucionais. O programa carrega um conjunto de imagens de treinamento, treina um modelo de rede neural convolucional e avalia o desempenho do modelo. O modelo treinado pode ser salvo em um arquivo para uso posterior.

## Requisitos

    Python 3.x
    Bibliotecas: cv2, numpy, os, sys, tensorflow, keras, sklearn

Certifique-se de ter todas as dependências instaladas antes de executar o programa.

Instalar as bibliotecas necessárias:

    pip install -r requirements.txt

## Uso

    python traffic.py data_directory [model.h5]

data_directory: O diretório que contém os dados de treinamento. O diretório deve ter uma pasta para cada categoria, numeradas de 0 a NUM_CATEGORIES-1. Dentro de cada pasta de categoria devem estar as imagens correspondentes.

model.h5 (opcional): O nome do arquivo para salvar o modelo treinado.

Se nenhum nome de arquivo for fornecido para o modelo treinado, o modelo não será salvo.

## Funcionalidades

O programa realiza as seguintes etapas:

1. Carrega as imagens e os rótulos de todas as imagens do diretório de dados.
 
2. Divide os dados em conjuntos de treinamento e teste.

3. Converte os rótulos em representação one-hot.

4. Constrói o modelo da rede neural convolucional.

5. Treina o modelo com os dados de treinamento.

6. Avalia o desempenho do modelo usando os dados de teste.

7. Salva o modelo treinado em um arquivo, se fornecido.

## Funções Principais

### load_data(data_dir)

Carrega os dados de imagem do diretório data_dir.

Assume-se que data_dir tenha uma pasta para cada categoria, numeradas de 0 a NUM_CATEGORIES-1. Dentro de cada pasta de categoria, há um número variável de arquivos de imagem.

Retorna uma tupla (images, labels). images é uma lista de todas as imagens no diretório de dados, onde cada imagem é formatada como um ndarray numpy com dimensões IMG_WIDTH x IMG_HEIGHT x 3. labels é uma lista de rótulos inteiros que representam as categorias de cada uma das imagens correspondentes.

### get_model()

Retorna um modelo de rede neural convolucional compilado. Assume-se que o input_shape da primeira camada seja (IMG_WIDTH, IMG_HEIGHT, 3). A camada de saída deve ter NUM_CATEGORIES unidades, uma para cada categoria.

O modelo é construído com as seguintes camadas:

1. Uma camada convolucional com 32 filtros, tamanho de kernel (3,3), padding "same" e ativação "relu".

2. Uma camada de max pooling com tamanho de pool (2,2).

3. Uma camada convolucional com 64 filtros, tamanho de kernel (3,3), padding "same" e ativação "relu".
   
4. Uma camada de max pooling com tamanho de pool (2,2).
   
5. Uma camada de achatamento.
   
6. Uma camada densa oculta com 256 unidades e ativação "relu".
    
7. Uma camada de dropout com taxa de dropout de 0.5.
    
8. Uma camada densa de saída com ativação "softmax" e NUM_CATEGORIES unidades.

O modelo é compilado com a função de perda "categorical_crossentropy", otimizador "adam" e métricas de avaliação "accuracy".

## Execução

Execute o programa usando o comando abaixo:

    ```
    python traffic.py data_directory [model.h5]
    ```

Substitua data_directory pelo diretório que contém os dados de treinamento. Você pode fornecer um nome de arquivo model.h5 opcional para salvar o modelo treinado.

O programa carregará os dados, treinará o modelo, avaliará seu desempenho e, se fornecido um nome de arquivo para o modelo, salvará o modelo treinado.

## Modelos e testagem para otimização 

    ```
    python traffic.py gtsrb
    ```
    
Primeiro, foi testado o número de camadas, de 1 a 3, e em seguida o número de filtros, de 16 a 64. Foi observado que com 2 camadas, uma com 32 filtros e outra com 64 filtros, em sequência, cada uma com pooling, apresentou melhor desempenho. Com mais de 2 camadas e com filtros acima de 64, a taxa de precisão diminuiu juntamente com a perda.

Após isso, foram testadas as camadas densas e de dropout. O número de unidades da camada densa variou de 128 a 256 e o valor de dropout variou de 0.3 a 0.5. Entre esses valores, o melhor desempenho foi obtido com 256 unidades na camada densa e dropout de 0.5.

Por fim, foram testados os otimizadores, variando de adam a rmsprop. Todos esses resultados estão mostrados na tabela abaixo, não incluindo todos os valores, apenas os mais significativos.

*=========================================================================*

|   | qt. layers |qt. pooling| dense | dropout|optimizer | loss  |accuracy|

| 1 | one 64     |    1		 |  128  |   0.5  |"rmsprop" |0.5132 | 0.8842 |

| 2 | two 32     |    1   	 |  128  |   0.5  |"rmsprop" |0.2242 | 0.9712 |

| 3 | two 32     |    1		 |  128  |   0.5  |"adam"    |0.2575 | 0.9368 |

| 4 | two 32     |    2   	 |  256  |   0.5  |"rmsprop" |0.3133 | 0.9403 |

| 5 | two 32 & 64|    2		 |  256  |   0.5  |"rmsprop" |0.2125 | 0.9703 |

| 6 | two 32 & 64|    2   	 |  256  |   0.5  |"adam"    |0.1024 | 0.9759 |

| 7 |  two 64    |    2		 |  256  |   0.5  |"rmsprop" |0.4387 | 0.9056 |

*=========================================================================*
