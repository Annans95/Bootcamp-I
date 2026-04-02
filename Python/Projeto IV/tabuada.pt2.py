print("Tabuada de multiplicação")
primeiro = int(input("Digite o valor do número base da tabuada: "))
for i in range(1, 11):

    resultado = primeiro * i
    print(f"{primeiro:2} x {i:2} = {resultado:3}")
