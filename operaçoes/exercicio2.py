# Verificador de número par ou ímpar
#Peça um número e diga se ele é:
#par
#ímpar
#Dica
#Use o operador de resto:

numero = int(input("Digite um numero: "))

if numero % 2 == 0: 
  print("Número par")
else: 
  print("Número ímpar")