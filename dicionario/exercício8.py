# Use o dicionário:

# produtos = {
#     "perfume": 120,
#     "shampoo": 25,
#     "sabonete": 8,
#     "creme": 35
# }
# Peça ao usuário o nome de um produto.
# - Se existir, mostre seu preço.
# - Se não existir, mostre "Produto não encontrado!".
# Conteúdos: dicionários, input(), if/else e in.

produtos = {
  "perfume": 120,
  "shampoo": 25,
  "sabonete": 8,
  "creme": 35
}

nome = input("Digite um produto: ")
if nome in produtos:
   print(f"o preço do {nome} é R$ {produtos[nome]}")
else:
   print("Produto não encontrado!!")   
   