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

produtos = {}

while True:
  
  nome = input("Digite o nome do Produto: ")
  preco = float(input(f"Digite o preço do {nome}: "))

  produtos[nome] = preco

  continuar = input("Deseja cadastrar outro produto? (sim ou não): ")

  if continuar.lower() in ("não", "nao"):
     break

# Mostrar todos os produtos
print("\nPordutos cadastrados:")
for nome, preco in produtos.items():
    print(f"Produto: {nome} | Preço: R${preco:.2f}")

#Valor total
total = 0
for preco in produtos. values():
    total += preco


print(f"\nValor total: R$ {total:.2f}")

#Produtos acima de R$50
print("\nProdutos acima de 50: ")
for nome, preco in produtos.items():
    if preco > 50:
       print(f"{nome} - R$ {preco:.2f}")


#pesquisar produto pelo nome
busca = input("\nDigite o nome do produto que deseja pesquisar: ")

if busca in produtos:
   print(f"{busca} custa R$ {produtos[busca]:.2f}")
else:
   print("Produto não encontrado!")   
   

