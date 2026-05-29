#Caixa Eletronico

#Mostrando o queo programa faz.
print("CAIXA ELETRÔNICO")
#valor total do usuário
saldo_total = float(10700)
#perguntando ao usuário sobre as opções e salvando na variavel "caixa_eletronico"
caixa_eletronico = int(input("Olar o que deseja? (Sacar(1) Depositar(2) Ver saldo(3)): "))
 
#Condições ao meu Código(Se o usuario escolher 1 ele revela as opções)
if caixa_eletronico == 1:
    saque = float(input("Qual valor quer sacar?: "))
    #se digitar 0 o programa diz valor incorreto
    if saque == 0:
        print("Valor incorreto!")
    elif saque > saldo_total:
        print("Valor recusado por saldo insuficiente!")
    else:
        saldo_total = saldo_total - saque
        print("Saque realizado com sucesso!")
        print("Saldo restante: R$", saldo_total)
# se usuário digitar a opção 2
elif caixa_eletronico == 2:
    deposito = float(input("Qual valor do depósito?: "))
    saldo_total = saldo_total + deposito
    print(f"R$ {deposito} foi depositado com sucesso!")
    print("Saldo atual: R$", saldo_total)
#Se o usuário digitar a opção 3
elif caixa_eletronico == 3:
    print("Seu saldo é: R$", saldo_total)






