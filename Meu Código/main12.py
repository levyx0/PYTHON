# Exercício 9 - Contador

# Crie uma lista:

# [10,8,5,3,2,20,15]

# Conte:

# Quantos são pares.
# Quantos são ímpares.
# Quantos são maiores que 10.

# Mostre:

# Pares: 4

# Ímpares: 3

# Maiores que 10: 2


print("CONTADOR")

contadorpar = 0
contadorimpar = 0
contadormaior10 = 0

numeros =[10, 22, 7, 19, 34, 5, 67, 8, 4, 2, 1, 3, 34, 66]

for numero in numeros:
      if numero % 2 == 0:
         print(numero)
         contadorpar +=1


      if numero % 2 == 1:
         print(numero)
         contadorimpar += 1


      if numero > 10:
         contadormaior10 +=1



print("Quantidades de números Pares: ", contadorpar)
print("Quantidade de números Ímpares: ", contadorimpar)
print("Quantidade de números maior que 10: ", contadormaior10)



