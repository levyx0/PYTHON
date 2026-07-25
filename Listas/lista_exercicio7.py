# Exercício 2 — Estoque de produtos
# Crie um menu com:
# Adicionar produto
# Remover produto
# Ver estoque
# Buscar produto (diz se está ou não no estoque)
# Sair
# 💡 Dica: append(), remove(), in, while True

print("ESTOQUE DE PRODUTOS")

produtos = []

while True:
    print("\n1 - ADICIONAR PRODUTO")
    print("2 - REMOVER PRODUTO")
    print("3 - VER ESTOQUE")
    print("4 - BUSCAR PRODUTO")
    print("0 - SAIR")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        produto = input("Digite o produto: ")
        produtos.append(produto)
        print("Produto adicionado!")

    elif opcao == "2":
        if len(produtos) == 0:
            print("Nenhum produto no estoque!")
        else:
            for i, produto in enumerate(produtos):
                print(f"{i} - {produto}")        # ← {produto} não {produtos}
            indice = int(input("Qual índice remover: "))  # ← fora do for
            produtos.pop(indice)
            print("Produto removido!")

    elif opcao == "3":
        if len(produtos) == 0:
            print("Nenhum produto no estoque!")
        else:
            print(f"\nTotal de produtos: {len(produtos)}")
            for i, produto in enumerate(produtos):
                print(f"{i + 1} - {produto}")

    elif opcao == "4":
        busca = input("Qual produto deseja buscar: ")
        if busca in produtos:
            print(f"{busca} está no estoque! ✓")
        else:
            print(f"{busca} não está no estoque! ✗")

    elif opcao == "0":
        print("Até logo!")
        break   

