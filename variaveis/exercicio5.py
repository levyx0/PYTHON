#Calculadora de salário
#Peça:
#nome do funcionário
#valor por hora
#horas trabalhadas
#Calcule o salário final.

nome = input("Digite seu nome: ")
valor_por_hora = int(input("Digite o valor da hora: "))  
horas_trabalhadas = int(input("Digite quantas olhas trabalhou: "))
resultado = valor_por_hora * horas_trabalhadas

print(f"{nome} recebe {resultado} de salario esse mês")