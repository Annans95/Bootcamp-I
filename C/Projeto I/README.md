# Verificador de Letras Repetidas

## Descrição
Este programa em C solicita ao usuário que digite uma palavra e verifica se há letras repetidas nela. Quando encontra uma letra que aparece mais de uma vez, o programa exibe qual letra se repetiu.

## Como funciona
1. O usuário digita uma palavra.
2. O programa percorre cada letra da palavra.
3. Se uma letra aparecer mais de uma vez, ela será exibida como repetida.

## Exemplo de uso
**Entrada:**

Digite uma palavra para verificar se ela é um palíndromo: banana

**Saída:**

a se repete
n se repete

## Tecnologias usadas
- Linguagem C  
- Biblioteca padrão `<stdio.h>`, `<string.h>` e `<locale.h>`  
- Compilador GCC

## Observação
Apesar da mensagem inicial mencionar "palíndromo", o programa atual apenas verifica letras repetidas. Não faz a verificação se a palavra é ou não um palíndromo.

