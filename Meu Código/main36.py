# Controle de estoque
# Fácil
# Crie um dicionário contendo 5 produtos e suas respectivas quantidades.
# Seu programa deverá:
# 1. Mostrar todos os produtos e quantidades.
# 2. Identificar produtos com estoque menor que 5.
# 3. Calcular a quantidade total de produtos em estoque.
# 4. Perguntar o nome de um produto.
# 5. Verificar se ele existe no dicionário.

#Criando o dicionário
estoque = {
  "perfume": 10,
  "shampoo": 3,
  "creme": 8,
  "sabonete": 2,
  "desodorante": 6
}

#Todos os produtos e quantidades
print("Estoque atual: ")
for produto, quantidade in estoque.items():
    print(produto, "-", quantidade)

#Produtos com estoque menor que 5
print("\nProdutos com estoque menor   que 5: ")
for produto, quantidade in estoque.items():
    if quantidade < 5:
        print(produto, "-", quantidade)


#Quantidade total.
total = 0
for produto, quantidade in estoque.items():
    total = total + quantidade
print("\nQuantidade total em estoque: ", total)    


#Perguntar e verificar
nome = input("\nDigite o nome do Produto: ")

if nome in estoque:
    print("Produto encontrado!")
else:
    print("Produto não encontrado!")     
    


    

