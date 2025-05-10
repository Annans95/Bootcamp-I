print('Calculadora Simples')
numero1=float(input('Digite o primeiro número:'))
operacao = input('Digite a operação (+, -, *, /): ')
numero2=float(input('Digite o segundo número:'))
if operacao == '+':
    print('Resultado:', numero1,'+',numero2,'=',numero1+numero2)
elif operacao == '-':
    print('Resultado:', numero1, '-',numero2,'=',numero1-numero2)
elif operacao == '*':
    print('Resultado:', numero1,'*',numero2,'=',numero1*numero2)
elif operacao == '/':
    if numero2 != 0:
        print('Resultado:', numero1, '/', numero2,'=',numero1/numero2)
    else:
        print("Erro: divisão por zero não permitida!")
else:
    print("Operação inválida!")