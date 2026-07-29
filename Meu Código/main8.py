# Crie uma lista:

# [8,15,20,33,42,50]

# Imprima somente os pares.

# No final mostre:

# Quantidade de pares: 4
#Coloque os ímpares

contadorpar = 0
contadorimpar = 0

numeros = [34, 8, 22, 44, 58, 30, 87, 31, 35, 21, 6, 3, 7, 27, 55, 49, 33, 51, 53, 67, 65]

for numero in numeros:
    if numero % 2 == 0:
       print(numero)
       contadorpar += 1

    if numero % 2 == 1:
       print(numero)
       contadorimpar += 1  
      

print("Quantidades de Pares: ", contadorpar)  
print("Quantidade de Ímpares: ", contadorimpar)  