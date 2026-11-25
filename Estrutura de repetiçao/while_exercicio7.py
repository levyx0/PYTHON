#Peça ao usuário um número e utilize while para mostrar a tabuada desse número de 1 até 10.

# Exemplo: usuário digita 5.
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 10 = 50

numero = int(input("Digite um número: "))

contador = 1

while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1