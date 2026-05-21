#Número par ou ímpar
#Crie um programa que:
#peça um número
#diga se é par ou ímpar
#pergunte se o usuário quer continuar
#O programa só termina quando o usuário responder:

while True:

   numero = int(input("Digite um número: "))

   if numero % 2 == 0:
      print("O número é par!")

   else:
      print("O número é ímpar!")

   continuar = input("Quer continuar?") 

   if continuar == "não":
      break