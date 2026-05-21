#Soma de números
#Peça números ao usuário e vá somando.

soma = 0

while True:

  numero = int(input("Digite um numero: "))

  if numero == 0:
    break

  soma += numero

print("Soma Total: ", soma)  