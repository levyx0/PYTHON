# Exercício 1 — Cadastro de Produtos

# Crie uma função chamada:

# cadastrar_produtos()

# Ela deve:

# Perguntar quantos produtos serão cadastrados.
# Para cada produto pedir:
# Nome
# Preço
# Armazenar tudo em um dicionário.
# Retornar esse dicionário.

# Depois crie outra função:

# mostrar_produtos(produtos)

# que mostre todos os produtos cadastrados.

def cadastrar_produtos():
    quantidade = int(input("Quantos produtos você vai cadastrar? "))

    produtos = {}

    for i in range(quantidade):
        nome = input(f"Nome do produto {i+1}: ")
        preco = float(input(f"Preço de {nome}: "))
        produtos[nome] = preco

    return produtos


def mostrar_produtos(produtos):
    for nome, preco in produtos.items():
        print(f"Produto: {nome} - Preço: R$ {preco:.2f}")


lista_produtos = cadastrar_produtos()
mostrar_produtos(lista_produtos)

