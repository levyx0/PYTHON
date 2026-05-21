#Tabuada
#eça um número ao usuário e mostre a tabuada dele de 1 até 10.

print("Tabuada")
numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)

