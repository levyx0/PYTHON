# Exercício 1 — Remover duplicatas
# Você recebeu a seguinte lista:

# numeros = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]

# 1. Transforme a lista em um conjunto.
# 2. Mostre o conjunto resultante.
# 3. Mostre quantos números únicos existem.
# Conceitos: set() e len().


numeros = [1, 2, 2, 2,  3, 4, 5, 5, 6, 6, 7]


#transformando a lista em conjunto.
conjunto = set(numeros)
#printando o conjunto
print(conjunto)
#mostrando quantos número únicos existem
print(len(conjunto))