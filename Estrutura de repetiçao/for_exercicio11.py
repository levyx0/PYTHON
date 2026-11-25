# Crie uma lista de produtos com seus preços. Utilize for para identificar os produtos que custam mais de R$ 50 e calcular o valor total desses produtos.

produtos = [
  ["Camiseta", 45.90],
  ["Calça jeans", 120.00],
  ["Tênis", 250.50],
  ["Meia", 15.00],
  ["Boné", 55.00],
  ["Cinto", 49.90]
]

total = 0

print("Produtos acima de r$ 50: ")
for produto in produtos:
  nome = produto[0]
  preco = produto[1]

  if preco > 50:
     print(f"-{nome}: R$ {preco:.2f}")
     total += preco

print(f"Valor total: R$ {total:.2f}")