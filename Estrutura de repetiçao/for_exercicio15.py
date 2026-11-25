#Maior e menor valor: dada a lista [45, 12, 89, 34, 7, 56, 23], encontre o maior e o menor número utilizando for, sem utilizar max() ou min().

numeros = [45, 12, 89, 34, 7, 56, 23]

maior = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print("Maior: ", maior)
print("Menor:", menor)