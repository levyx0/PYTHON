# Em Python, conjuntos (sets) são estruturas de dados usadas para armazenar elementos únicos, sem repetição.

frutas = {"Maçã", "Uva", "Banana"}
print(frutas)

#não permite elementos duplicados
numeros = {1, 2 , 2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 9}
print(numeros)

#adcionando elementos
nomes = {"Marcos", "João"}
nomes.add("Paulo")
print(nomes)

#Operações matemáticas com conjuntos.

#União
#junta os elementos dos dois conjuntos.

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)


#interseção 
#mostra os elementos  em comum.

a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)

#Diferença
#mostra  o que existe em um conjunto e não no outro.

a = {1, 2, 3}
b = {3, 4, 5}
print(a - b)

#Difernça Simétrica
#Mostra elementos que não são comuns.

a = {1, 2, 3}
b = {3, 4, 5}
print(a ^ b)

#Convertendo lista para conjunto
#Muito usado para remover duplicados.

lista = [1, 2, 2, 3, 3, 4, 4, 5]
conjunto = set(lista)
print(conjunto)


#Criar conjunto vazio:
conjunto = set()


#Removendo elementos:
frutas = {"maçã", "banana", "uva"}
frutas.remove("banana")
print(frutas)


#discard() — remove o elemento se ele existir, mas não gera erro se ele estiver ausente.

frutas = {"maçã", "uva"}
frutas.discard("banana") # sem erro, mesmo que nao exista
print(frutas)


#Verificando se um elemento existe
produtos = {"Perfumes", "Sabonete", "Shampoo"}

if "Perfumes" in produtos:
    print("Produto Encontrado!")
else:
    print("Produto não Encontrado!")




#Pecorrendo um conjunto com for
#também podemos percorrer os elementos de um conjuto.

nomes = {"João", "Maria", "Pedro", "Ana"}

for nome in nomes:
    print(nome)



#O programa imprime todos os nomes, mas a ordem não é garantida.

#Conjunto  X  Lista
#Em conjuto você não acessa os elementos por posição.

# nomes = {"João", "Maria", "Pedro"}
# print(nomes[0])

#Esse código gera erros, pois conjuntos naão permitem acesso por índice.



#Removendo duplicatas de uma lista.


produtos = [
    "perfumes",
    "shampoo",
    "perfume",
    "sabonete",
    "shampoo"
]

produtos_unicos = set(produtos)
print(produtos_unicos)

#O set() transforma a lista em um conjunto, eliminando as duplicatas.

#Se depois precisar voltar para uma lista:
produtos_unicos = list(set(produtos))
