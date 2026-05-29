# Removedor de duplicatas
# Peça ao usuário para digitar 8 números. Armazene em uma lista e no final exiba apenas os números  sem repetição, mantendo a ordem em que apareceram.
# Entrada: [3, 1, 4, 1, 5, 3, 2, 5]
# Saída:   [3, 1, 4, 5, 2]
# 💡 Dica: count() ou verificar if item not in lista

#Cria lista vazia para guardar os 8 números
numeros = []


# 2. Pede 8 números ao usuário
for i  in  range(8):
    numero = float(input(f"Digite o {i + 1} número: "))
    numeros.append(numero)


#Cria uma nova lista vazia para guardar sem duplicatas
sem_duplicatas = []    

# 4. Percorre a lista original
for numero in numeros:
    if numero not in sem_duplicatas:  # se o número NÃO está na nova lista
        sem_duplicatas.append(numero) # adiciona



print("Lista Original: ", numeros)
print("Lista sem Duplicatas: ", sem_duplicatas)
