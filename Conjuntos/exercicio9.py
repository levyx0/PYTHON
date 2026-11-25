#Filtrar números pares e ímpares
#numeros = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]

# Percorra a lista e crie dois conjuntos:
# - Um com os números pares.
# - Outro com os números ímpares.
# Ao final, mostre os conjuntos e a quantidade de elementos únicos de cada um.
# Conceitos: for, if/else, %, set() e len().

numeros = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10]

numeros_pares = set()
numeros_impares = set()

for numero in  numeros:
    if numero % 2 == 0:
        numeros_pares.add(numero)
    else:
        numeros_impares.add(numero)  

print(f"Números Pares: {numeros_pares}", len(numeros_pares))
print(f"Números ìmpares: {numeros_impares}", len(numeros_impares))


