#Calculadora de idade futura
#Peça:
#nome
#idade atual
#Depois pergunte:
#quantos anos no futuro
#E mostre a idade futura.

nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))

anos_futuros = int(input("Quantos anos no futuro?: "))
idade_futura = idade + anos_futuros

print(f"{nome} terá {idade_futura} anos daqui a {anos_futuros} anos.")


