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


