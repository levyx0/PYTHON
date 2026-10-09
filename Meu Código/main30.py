#Maior número da lista

def maior_numero(numeros):
    maior = numeros[0]

    for numero in numeros:
        if numero > maior:
            maior = numero

    return maior

lista = [10, 25, 4, 67, 88, 15]
resultado = maior_numero(lista)
print(f"O maior número da lista é: {resultado}")    




#Procurar Produto

def procurar_produtos(produtos, produto):
    if produto in produtos:
        return("Produto Encontrado!!")
    else:
        return("Produto não Encontrado!")

produtos = ["perfume", "shampoo", "sabonete", "creme"]

print(procurar_produtos(produtos, "perfume"))
print(procurar_produtos(produtos, "tenis"))


