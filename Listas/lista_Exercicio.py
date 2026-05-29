# Exercício 1 — Lista de compras
# Crie um programa onde o usuário pode:
# Adicionar itens à lista
# Ver todos os itens
# Sair
# Exiba a lista numerada e mostre quantos itens tem no total.
# 💡 Dica: append(), len(), enumerate()


print("LISTAS DE COMPRAS")

print("LISTA DE COMPRAS")

compras = []

while True:
    print("\n1 - Adicionar compra")
    print("2 - Remover compra")
    print("3 - Ver lista de compras")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        compra = input("Qual compra deseja adicionar: ")
        compras.append(compra)
        print("Compra adicionada!")

    elif opcao == "2":
        if len(compras) == 0:
            print("Nenhuma compra adicionada!")
        else:
            for i, compra in enumerate(compras):
                print(f"{i} - {compra}")
            indice = int(input("Qual índice remover?: "))
            compras.pop(indice)
            print("Compra removida!")

    elif opcao == "3":
        if len(compras) == 0:
            print("Nenhuma compra adicionada!")
        else:
            print(f"\nTotal de itens: {len(compras)}")
            for i, compra in enumerate(compras):
                print(f"{i + 1} - {compra}")

    elif opcao == "0":
        print("Até logo!")
        break                

                  