# Nim Game

Este é um código Python que implementa o jogo Nim, juntamente com uma IA treinada para jogar contra um jogador humano. O jogo Nim é um jogo de estratégia no qual os jogadores retiram objetos de pilhas, seguindo certas regras, até que um jogador seja forçado a retirar o último objeto, tornando o outro jogador o vencedor.

## Como Jogar

    1. Certifique-se de ter o Python instalado em seu sistema.
    2. Execute o arquivo nim.py para ter acesso às classes Nim e NimAI.
    3. A classe Nim representa o jogo em si, com métodos para inicializar o tabuleiro, fazer movimentos e verificar o vencedor.
    4. A classe NimAI implementa uma IA usando aprendizado por reforço com o algoritmo Q-Learning. Ela é capaz de aprender e tomar decisões com base nas jogadas anteriores.
    5. O método train(n) treina a IA executando n jogos contra ela mesma. Quanto mais jogos forem executados, melhor será o desempenho da IA.
    6. O método play(ai, human_player) permite que um jogador humano jogue contra a IA treinada. O jogador humano pode escolher ser o primeiro ou o segundo a jogar.

## Como Executar

    1. Certifique-se de ter o Python instalado em seu sistema.
    2. Execute o arquivo 
    ```
    python play.py
    ```
    3. A IA será treinada com 10.000 jogos. Você pode ajustar esse número no código se desejar.
    4. Após o treinamento, você poderá jogar contra a IA. Siga as instruções no console para fazer seus movimentos.
    5. O jogo continuará até que haja um vencedor. O resultado será exibido no console.