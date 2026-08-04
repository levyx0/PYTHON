# Encontrando o maior

# Sem usar:

# max()

# Descubra:

# maior número
# menor número

# da lista:

# [10,25,8,100,5,70,42]



print("ACHE O MAIOR E O MENOR NÚMERO")


lista = [27, 32, 29, 40, 59, 190, 47, 2, 1]

maior = lista[0]
menor = lista[0]

for numero in lista:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

print(f"O Maior número é: {maior}")
print(f"O Menor número é : {menor} ")
            