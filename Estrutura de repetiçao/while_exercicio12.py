# . Calculadora com menu
# Crie um menu que fique aparecendo até o usuário escolher sair.
# 1 - Somar
# 2 - Subtrair
# 3 - Multiplicar
# 4 - Dividir
# 5 - Sair
# O programa deve solicitar dois números e executar a operação escolhida.

opcao = 0

while opcao != 5:
    print("\n---CALCULADORA ---")
    print("1 - somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 5:
        print("Encerrando o programa. Até Logo!")
    elif opcao >= 1 and opcao <= 4:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if opcao == 1:
            print(f"Resultado: {a} + {b} = {a + b}")
        elif opcao == 2:
            print(f"Resultado: {a} - {b} = {a - b}")
        elif opcao == 3:
            print(f"Resultado: {a} x {b} = {a * b}")  
        else:
            if b == 0:
                print("Erro: não é possível dividir por zero.")
            else:
                print(f"Resultado: {a} / {b} = {a / b}")
    else:
        print("Opção Inválida. Tente de novo.")
