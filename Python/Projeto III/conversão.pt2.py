print("Tabela de Conversão de Fahrenheit para Celsius")
inicial=int(input("Digite o valor inicial em Fahrenheit:"))
final=int(input("Digite o valor final em Fahrenheit:"))
print("Fahrenheit|\tCelsius")
if inicial<=final:
    for f in range(inicial, final+1, 1):
        c = 5 * (f - 32)/9
        print(f"{f}°f\t|{c:.2f}°C")
else:
    for f in range(inicial,final-1, -1):
        c = 5 * (f - 32) / 9
        print(f"{f}°f\t|{c:.2f}°C")