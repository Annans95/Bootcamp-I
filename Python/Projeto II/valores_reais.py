ct=0
soma=0
m=0
media=0
print('Programa que conta valores digitados, calcula a média e verifica quantos são maiores que 20')
print('Digite [-1] para sair')
while True:
    numero=float(input('Digite um número real:'))
    if numero == -1:
        break
    ct=ct+1
    soma=soma+numero
    if numero >20:
        m=m+1
if ct > 0:
    media=soma/ct
print('Quantidade de valores digitados:',ct)
print('Soma dos valores digitados:',soma)
print('Média aritmética dos valores digitados:',media)
print('A quantidade de valores digitados maior que 20:',m)

