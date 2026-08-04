# Exercício 8 - Sistema de notas

# Peça o nome de cinco alunos.

# Depois peça a nota de cada um.

# No final mostre:

# João -> 8

# Maria -> 10

# Carlos -> 6

# Depois informe:

# Aprovado

# ou

# Reprovado

# para cada aluno.

print("Sistemas de Notas")

nome1 = input("Escreva o nome do Aluno: ")
nota1 = float(input("Diga a nota do Aluno: "))

nome2 = input("Escreva o nome do Aluno: ")
nota2 = float(input("Diga a nota do aluno: "))

nome3 = input("Escreva o nome do Aluno: ")
nota3 = float(input("Diga a nota do aluno: "))

nome4 = input("Escreva o nome do Aluno: ")
nota4 = float(input("Diga a nota do aluno: "))

nome5 = input("Escreva o nome do Aluno: ")
nota5 = float(input("diga o nota o aluno: "))

print(f"O Aluno: {nome1} tirou a nota: {nota1}")
if nota1 >= 7:
   print("O aluno Passou!! Parabéns!!")
else:
   print("O aluno não passou!!!")   


print(f"O Aluno: {nome2} tirou a nota: {nota2}")
if nota2 >= 7:
   print("O aluno Passou !!! Parabéns!!")
else:
   print("O aluno não passou!!")


print(f"O Aluno: {nome3} tirou a nota: {nota3} ")
if nota3 >= 7:
   print("O aluno passou!!! Parabéns !!!")   
else:
   print("O aluno não passou!!")


print(f"O Aluno: {nome4} tirou a nota: {nota4}")
if nota4 >= 7:
   print("O aluno passou!!! Parabéns!!!!")
else:
   print("O aluno não passou!!!")


print(f"O Aluno: {nome5} tirou nota: {nota5}")     
if nota5 >= 7:
   print("O aluno Passou!! Parabéns!!!")
else:
   print("O aluno não passou!!")
               