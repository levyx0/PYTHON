#Encontrar elementos em comum
# Crie uma função chamada encontrar_comuns(lista1, lista2) que:
# 1. Receba duas listas.
# 2. Transforme as listas em conjuntos.
# 3. Retorne os elementos que aparecem nas duas listas.
# Teste com:
# lista1 = [1, 2, 3, 4, 4, 5]
# lista2 = [3, 4, 5, 6, 7]
#Conceitos: funções, parâmetros, return, listas e conjuntos.

lista1 = [1, 2, 3, 4, 4, 5]
lista2 = [3, 4, 5, 6, 7]

#criando a função
def encontrar_comuns(lista1, lista2):
    conj1 = set(lista1)
    conj2 = set(lista2)

    return conj1 & conj2

resultado = encontrar_comuns(lista1, lista2)
print(resultado)