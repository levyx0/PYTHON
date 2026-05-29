#Lista é uma estrutura que armazena vários valores em uma única variável, em ordem.

#Listas de  números:
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Listas de strings:
frutas = ["maçã", "banana", "melancia", "melão"]

#lista mista(pode misturar tipos)
mista = [1, "Marcos", 1.99, True]

#Lista vazia
vazia = []


#Acessando elementos:

frutas = ["maçã", "banana", "uva", "manga"]
#           0        1        2       3      → índices positivos
#          -4       -3       -2      -1      → índices negativos

frutas[0]    # "maçã"   → primeiro elemento
frutas[-1]   # "manga"  → último elemento
frutas[1:3]  # ["banana", "uva"] → fatiamento
frutas[:2]   # ["maçã", "banana"]
frutas[2:]   # ["uva", "manga"]


#Modificando elementos:

frutas = ["maçã", "banana", "uva"]

frutas[1] = "morango"   # substitui "banana" por "morango"
print(frutas)           # ["maçã", "morango", "uva"]


#adcionando Elementos: 

frutas = ["maçã", "banana"]

frutas.append("uva")         # adiciona no final → ["maçã", "banana", "uva"]
frutas.insert(1, "morango")  # adiciona na posição 1 → ["maçã", "morango", "banana", "uva"]
frutas.extend(["kiwi", "melão"]) # junta outra lista no final

#Removendo Elementos:

frutas.remove("banana")  # remove pelo valor
frutas.pop()             # remove e retorna o último elemento
frutas.pop(1)            # remove e retorna o elemento da posição 1
frutas.clear()           # remove todos os elementos


#Buscando elementos:

frutas = ["maçã", "banana", "uva", "banana"]

frutas.index("banana")   # 1     → posição da primeira ocorrência
frutas.count("banana")   # 2     → quantas vezes aparece
"uva" in frutas          # True  → existe na lista?

#Ordenando:
 
numeros = [3, 1, 4, 1, 5, 9, 2]

numeros.sort()             # ordena crescente → [1, 1, 2, 3, 4, 5, 9]
numeros.sort(reverse=True) # ordena decrescente → [9, 5, 4, 3, 2, 1, 1]
numeros.reverse()          # inverte a ordem
sorted(numeros)            # retorna nova lista ordenada sem modificar a original

#Outras operações:

frutas = ["maçã", "banana", "uva"]

len(frutas)       # 3         → tamanho da lista
frutas.copy()     # cria uma cópia da lista

# Percorrendo listas:

frutas = ["maçã", "banana", "uva"]

# Jeito simples
for fruta in frutas:
    print(fruta)

# Com índice (enumerate)
for indice, fruta in enumerate(frutas):
    print(indice, "-", fruta)
# 0 - maçã
# 1 - banana
# 2 - uva


# Listas aninhadas (matriz):

# Lista dentro de lista
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz[0]       # [1, 2, 3]    → primeira linha
matriz[1][2]    # 6            → linha 1, coluna 2

# Percorrendo matriz
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()
# 1 2 3
# 4 5 6
# 7 8 9

# List Comprehension — jeito pythônico de criar listas

# Jeito tradicional
quadrados = []
for i in range(1, 6):
    quadrados.append(i * i)

# Com list comprehension (mais elegante)
quadrados = [i * i for i in range(1, 6)]
# [1, 4, 9, 16, 25]

# Com condição
pares = [i for i in range(10) if i % 2 == 0]
# [0, 2, 4, 6, 8]




# 🆚 Resumo dos métodos:           O que faz:
# append(x)                      Adciona no final
#insert(i, x)                    adciona na posição i.
#extend(lista)                   Junta outra Lista
#remove(x)                       Remove pelo valor
#pop(i)                          Remove pela posição
#index(x)                        Retorna a posição do valor
#count(x)                        Conta ocorrências
#sort()                          Ordena a Lista
#reverse()                       Inverte a ordem
#clear()                         Limpa a lista
#copy()                          cria uma cópia
#len()                           retorna o tamanho