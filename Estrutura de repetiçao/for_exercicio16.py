# Tabuada: peça um número ao usuário e utilize for para mostrar sua tabuada de 1 até 10.

numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")