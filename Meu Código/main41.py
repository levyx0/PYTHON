# Sistema de caixa de uma loja
# Imagine que você trabalha no caixa de uma loja.
# Crie um programa que permita cadastrar produtos e seus preços em uma lista de dicionários.
# Exemplo:
# produtos = [
#     {"nome": "Perfume", "preco": 120},
#     {"nome": "Creme", "preco": 35}
# ]
# O programa deverá:
# 1. Permitir adicionar produtos.
# 2. Mostrar todos os produtos cadastrados.
# 3. Calcular o valor total dos produtos.
# 4. Verificar quais produtos custam mais de R$ 50.
# 5. Permitir pesquisar um produto pelo nome.
# Assuntos: listas, dicionários, strings, while, if/else, operações.



#Feito novamente , mas melhorado:

def ler_preco(nome):
    while True:
        try:
            preco = float(input(f"Digite o preço do {nome}: "))
            if preco >= 0:
                return preco
            print("O preço não pode ser negativo.")
        except ValueError:
            print("Digite um número válido (use ponto: 35.50).")

def cadastrar_produtos():
    produtos = {}

    while True:
        nome = input("Digite o nome do produto: ").strip()
        if nome == "":
            print("O nome não pode ser vazio.")
            continue

        produtos[nome] = ler_preco(nome)

        continuar = input("Deseja cadastrar outro produto? (sim ou não): ").lower()
        if continuar in ("não", "nao", "n"):
            break

    return produtos

def mostrar_produtos(produtos):
    print("\nProdutos cadastrados:")
    for nome, preco in produtos.items():
        print(f"Produto: {nome} | Preço: R$ {preco:.2f}")

def calcular_total(produtos):
    return sum(produtos.values())

def produtos_acima(produtos, limite):
    acima = {}
    for nome, preco in produtos.items():
        if preco > limite:
            acima[nome] = preco
    return acima

def pesquisar_produto(produtos, busca):
    for nome, preco in produtos.items():
        if nome.lower() == busca.lower():
            return preco
    return None

# Programa principal
produtos = cadastrar_produtos()

mostrar_produtos(produtos)
print(f"\nValor total: R$ {calcular_total(produtos):.2f}")

print("\nProdutos acima de R$ 50:")
for nome, preco in produtos_acima(produtos, 50).items():
    print(f"{nome} - R$ {preco:.2f}")

busca = input("\nDigite o nome do produto que deseja pesquisar: ")
preco = pesquisar_produto(produtos, busca)

if preco is None:
    print("Produto não encontrado!")
else:
    print(f"{busca} custa R$ {preco:.2f}")