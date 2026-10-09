# Exercício 5 — Números pares

# Crie:

# numeros = [1, 4, 7, 10, 13, 16, 20, 25]

# Percorra a lista e mostre somente os números pares.

# 💡 Dica: use %.

numeros = [1 , 4, 7, 10, 16, 20, 25 , 33, 47, 52]

for numero in numeros:
     if numero % 2 == 0:
         print(numero)