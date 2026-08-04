# Caixa de supermercado

# Crie um dicionário:

# produtos = {
#     "Arroz": 20,
#     "Feijão": 15,
#     "Macarrão": 8,
#     "Óleo": 12,
#     "Açúcar": 7
# }

# Pergunte ao usuário:

# Quantos produtos deseja comprar?

# Depois pergunte o nome do produto essa quantidade de vezes.

# No final mostre:

# Produtos comprados

# Arroz - R$ 20
# Óleo - R$ 12
# Macarrão - R$ 8

# Total: R$ 40

# Desafio extra

# Se o produto não existir:

# Produto não encontrado.


print("SUPERMERCADO")

total = 0

produtos = {
  "arroz": 25,
  "açucar": 20,
  "sal": 5,
  "feijão": 10,
  "macarrão": 15,
  "óleo": 7,
  "manteiga": 6,
  "biscoito": 15,
  "nescau": 8,
  "café": 10
}


quantidade = int(input("Quantos produtos deseja comprar?: "))

for i in range(quantidade):
    mercado = input(f"Digite o nome do produto {i + 1}: ")
    if mercado in produtos:
        print(f"Produto: {mercado}")
        print(f"Preço: R$ {produtos[mercado]}")
        print(produtos[mercado])
        total += produtos[mercado]

    else:
        print("produto não encontrado")    


print(f"Total da compra: R$ {total}")        