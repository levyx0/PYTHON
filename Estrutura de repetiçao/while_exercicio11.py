# Adivinhe o número
# Crie uma variável com um número secreto, por exemplo, 27.
# Peça ao usuário para tentar adivinhar.
# - Se errar, informe se o número secreto é maior ou menor que o palpite.
# - Se acertar, mostre uma mensagem de parabéns.
# - Conte quantas tentativas foram necessárias.

secreto = 27
tentativas = 0

palpite = int(input("Advinhe o número: " ))
tentativas = tentativas + 1

while palpite != secreto:
    if palpite < secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")
    palpite = int(input("tente de novo: "))
    tentativas = tentativas + 1 


print(f"Parabens! Você acertou em {tentativas} tentativa(s).")
