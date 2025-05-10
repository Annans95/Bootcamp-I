# Jogo da Adivinhação 

## Descrição

Este é um jogo simples de adivinhação desenvolvido em linguagem C. O programa gera um número aleatório entre 1 e 100 e desafia o usuário a adivinhar esse número, informando se cada tentativa foi muito alta ou muito baixa até o acerto.

## Funcionalidades

- Geração de número aleatório entre 1 e 100.
- Interação com o usuário por meio do terminal.
- Dicas após cada tentativa ("Muito Alto!" ou "Muito Baixo!").
- Contador de tentativas.
- Mensagem final ao acertar o número.

## Como usar

1. Compile o código com um compilador C (como `gcc`):
   ```bash
   gcc jogo_adivinhacao.c -o jogo

2. Execute o programa:

./jogo


3. Tente adivinhar o número digitando valores entre 1 e 100.


4. Continue tentando até acertar. O programa mostrará quantas tentativas você usou.



##  Exemplo de uso

Jogo da Adivinhação

Digite a sua tentativa de 1 a 100: 50

Muito Baixo!

Você errou, digite novamente: 75

Muito Alto!

Você errou, digite novamente: 63

Muito Baixo!

Você errou, digite novamente: 70

Você acertou! Número de tentativas: 4

## Tecnologias utilizadas

Linguagem C

stdio.h – Entrada e saída de dados

locale.h – Suporte à acentuação

stdlib.h – Geração de números aleatórios

time.h – Obtenção da hora atual para gerar aleatoriedade


## Autoras

Anna Nicolly da Silva

[[Anne Caroline Gonçalves de Mesquita](https://github.com/anne-cgm)]
