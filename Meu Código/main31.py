#Crie uma função: Ela deve percorrer a lista e mostrar:Produto: perfume
# Produto: shampoo
# Produto: sabonete


def verificar_produtos(produtos):
    for produto in produtos:
        print("Produto:", produto)

def verificar_produto(produtos, nome):
    if nome in produtos:
        print(f"O produto {nome} está disponível.")
    else:
        print(f"O produto {nome} não está disponível.")

produtos = ["perfume", "shampoo", "sabonete"]

verificar_produtos(produtos)
verificar_produto(produtos, "perfume")
verificar_produto(produtos, "creme")