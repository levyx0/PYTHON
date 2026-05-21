# ============================================
#           CALCULADORA INTERATIVA
# ============================================

import math  # biblioteca para operações avançadas

# ── Funções de cálculo ──────────────────────

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    # Divisão por zero causa erro, então verificamos antes
    if b == 0:
        return "Erro: não é possível dividir por zero!"
    return a / b

# ── Menu principal ──────────────────────────

def mostrar_menu():
    print("\n=============================")
    print("       CALCULADORA           ")
    print("=============================")
    print("  1 - Somar")
    print("  2 - Subtrair")
    print("  3 - Multiplicar")
    print("  4 - Dividir")
    print("  0 - Sair")
    print("=============================")

# ── Pedir os números ────────────────────────

def pedir_numeros():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    return a, b  # retorna os dois valores juntos

# ── Loop principal ──────────────────────────
# O programa fica rodando até o usuário digitar 0

while True:
    mostrar_menu()

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("\nAté logo!")
        break  # encerra o while

    elif opcao in ["1", "2", "3", "4"]:
        a, b = pedir_numeros()  # recebe os dois números

        if opcao == "1":
            resultado = somar(a, b)
            operacao = "+"
        elif opcao == "2":
            resultado = subtrair(a, b)
            operacao = "-"
        elif opcao == "3":
            resultado = multiplicar(a, b)
            operacao = "*"
        elif opcao == "4":
            resultado = dividir(a, b)
            operacao = "/"

        # Exibe o resultado formatado
        print(f"\n  {a} {operacao} {b} = {resultado}")

    else:
        print("\nOpção inválida! Tente novamente.")


    
    
