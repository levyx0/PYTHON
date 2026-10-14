#Estoque e valor total
#Use este dicionário:

# estoque = {
#     "perfume": 10,
#     "shampoo": 20,
#     "sabonete": 30,
#     "creme": 5
# }

estoque = {
  "perfume": 10,
  "shampoo": 20,
  "sabonete": 30,
  "creme": 5
}

for produto, quantidade in estoque.items():
    print(produto, "-", quantidade)

total = 0
for produto, quatidade in estoque.items():
    total = total + quantidade
print("\nTotal de itens no estoque: ", total)

print("\nProdutos com menos de 10 unidades: ")
for produto, quantidade in estoque.items():
    if quantidade < 10:
        print(produto)
