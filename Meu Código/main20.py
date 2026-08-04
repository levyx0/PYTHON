# Sistema bancário

# Saldo inicial:

# saldo = 1000

# Mostre um menu:

# 1 - Depositar

# 2 - Sacar

# 3 - Ver saldo

# 4 - Sair

# Dependendo da opção:

# deposita
# saca
# mostra saldo

# Se sacar mais do que possui:

# Saldo insuficiente.


print("SISTEMA BANCÁRIO")

Saldo_total = float(10000)

sistema_bancario = int(input("Olá o que desja? (Sacar(1) Depositar(2) Saldo(3) Sair(4)): "))

#se a pessoa digitar a opção 1
if sistema_bancario == 1:
   saque = float(input("Qual valor que deseja sacar?: "))
   if saque == 0:
      print("Valor incorreto")
   elif saque > Saldo_total:
      print("Valor recusado!!! Saldo Insuficiente.!")
   else:
      Saldo_total = Saldo_total - saque
      print("  Valor sacado com sucesso!!!")   
      print(f"Saldo restante:  {Saldo_total}")


#Se o usuário digitar a opção 2 
elif sistema_bancario == 2:
    deposito = float(input("Qual valor deseja depositar?: "))    
    Saldo_total = Saldo_total + deposito
    print(f"R$ {deposito} foi depositado com sucesso!!")
    print(f"Saldo atual: {Saldo_total}")


#Se on usuário digitar a opção 3
elif sistema_bancario == 3:
     print(f"O seu Saldo atual é: {Saldo_total}")    

#Se o usuário digitar a opção 4
elif sistema_bancario == 4:
     print("Obrigado!! volte sempre!!!")     
