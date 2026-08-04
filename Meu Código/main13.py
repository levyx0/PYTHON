# Mini Mercado

# Crie um dicionário:

# {
#     "Arroz": 25,
#     "Feijão": 18,
#     "Macarrão": 10,
#     "Açúcar": 8,
#     "Óleo": 12
# }

# Pergunte ao usuário:

# Qual produto deseja comprar?

# Se existir:

# Produto encontrado.

# Preço: R$ 25

# Caso contrário:

# Produto não encontrado.


print("MERCADO")


produtos = {
  "Arroz": 20,
  "Óleo": 10,
  "Açucar": 15,
  "Macarrão": 10,
  "Vinagre": 14,
  "Manteiga": 8,
  "Sal": 5,
  "Biscoito": 20
}

mercado = input("Qual produto do nosso mercado você deseja comprar?: ")
if mercado in produtos:
   print("Produto Encontrado!!")
   print("Preço: ", produtos[mercado])
else:
   print("Produto não encontrado!")   

