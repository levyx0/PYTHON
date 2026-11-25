#O while é uma estrutura de repetição do Python. Ele permite executar um bloco de código repetidamente enquanto uma condição for verdadeira (True).

# Como funciona o while?
# A estrutura básica é:
# while condição:
#     # código que será repetido

#primeiro exemplo: contador
# Imagine que você queira imprimir os números de 1 até 5.

contador = 1

while contador <= 5:
    print(contador)
    contador += 1


#Vamos entender cada parte:
#contador = 1 (Criamos uma variável que começa com o valor 1.)
#while contador <= 5:(Enquanto o contador for menor ou igual a 5, o código continuará executando.)
#print(contador)(Mostra o número atual.)
#contador += 1(Aumenta o contador em 1.)
#Atenção: essa última linha é fundamental. Sem ela, o contador nunca aumentaria e o laço poderia ficar infinito.

#Usando while com input()
#Imagine que você queira solicitar uma senha até o usuário acertar.

senha = ""

while senha != "1234":
    senha = input("Digite sua senha: ")

print("Acesso Permitido!")


# Como funciona?
# - A senha começa vazia.
# - O programa pergunta a senha.
# - Se estiver errada, o while continua.
# - Se estiver correta, a condição se torna falsa.
# - O programa sai do laço.
# Esse tipo de estrutura é muito utilizado em validações e sistemas de login.


#Usando while para criar menus
# Imagine um programa com três opções:
# 1. Cadastrar produto.
# 2. Mostrar produtos.
# 3. Sair.
# Podemos fazer assim:

produtos = {}
while True:
    print("\n---Menu---")
    print("1 - Cadastrar produto")
    print("2 - Mostrar produtos")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))

        produtos[nome] = preco

        print("Produto cadastrado!")
    elif opcao == "2":
        for nome, preco in produtos.items():
            print(f"{nome}: R$ {preco:.2f}")
    elif opcao == "3":
        print("Ecerrando o programa...")
        break
    else:
        print("Opção inválida")       
