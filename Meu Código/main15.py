# Cadastre 5 alunos.

# Cada aluno possui:

# nome
# idade
# nota

# Guarde tudo em uma lista de dicionários.

# Depois mostre:

# Nome: João
# Idade: 20
# Nota: 8.5
# Situação: Aprovado

# No final mostre:

# quantidade de aprovados
# quantidade de reprovados
# média da turma


aprovados = 0
reprovados = 0


print("Bem vindo ao cadastro de Aluno")

print("Por favor digite o nome de 5 alunos de sua turma e as notas deles para dizer se eles passaram ou não e a média da turma")

aluno1 = input("Me diga o nome do Primeiro aluno: ")
aluno2 = input("Me diga o nome do Segundoa aluno: ")
aluno3 = input("Me diga o nome do Terceiro aluno:")
aluno4 = input("Me diga o nome do Quarto aluno: ")
aluno5 = input("Me diga o nome do Quinto aluno: ")

idade1 = int(input(f"Me diga a idade de {aluno1}: "))
idade2 = int(input(f"Me diga a idade de {aluno2}: "))
idade3 = int(input(f"Me diga a idade de {aluno3}: "))
idade4 = int(input(f"Me diga a idade de {aluno4}: "))
idade5 = int(input(f"Me diga a idade de {aluno5}: "))


nota1 = float(input(f"Me diga a nota de {aluno1}: "))
nota2 = float(input(f"Me diga a nota de {aluno2}: "))
nota3 = float(input(f"Me diga a nota de {aluno3}: "))
nota4 = float(input(f"Me diga a nota de {aluno4}: "))
nota5 = float(input(f"Me diga a nota de {aluno5}: "))


alunos = {
  "aluno1": aluno1,
  "idade1": idade1,
  "nota1": nota1,

  "aluno2": aluno2,
  "idade2": idade2,
  "nota2": nota2,

  "aluno3": aluno3,
  "idade3": idade3,
  "nota3": nota3,

  "aluno4": aluno4,
  "idade4": idade4,
  "nota4": nota4,

  "aluno5": aluno5,
  "idade5": idade5,
  "nota5": nota5
}



media = (alunos["nota1"] + alunos["nota2"] + alunos["nota3"] + alunos["nota4"] + alunos["nota5"]) /  5




print("Nome: ", alunos["aluno1"])
print("Idade: ", alunos["idade1"], "anos")
print("Nota: ", alunos["nota1"])

if nota1 >= 7:
   print(f"O aluno: {aluno1} passou!!")
   aprovados +=1
else:
   print(f"O aluno: {aluno1} não passou!!")
   reprovados +=1 


print("Nome: ", alunos["aluno2"])
print("Idade: ", alunos["idade2"])
print("Nota: ", alunos["nota2"] ) 

if nota2 >= 7:
   print(f"O aluno: {aluno2} passou!!")
   aprovados +=1
else:
   print(f"O aluno: {aluno2} não passou !!!")
   reprovados +=1



print("Nome: ", alunos["aluno3"])
print("Idade: ", alunos["idade3"]) 
print("Nota: ", alunos["nota3"])     

if nota3 >= 7:
   print(f"O aluno: {aluno3} passou!!")
   aprovados +=1
else:
   print(f"O aluno: {aluno3} não passou !!!")
   reprovados +=1



print("Nome: ", alunos["aluno4"]) 
print("Idade:", alunos["idade4"])
print("Nota: ", alunos["nota4"])

if nota4 >= 7:
   print(f"O aluno: {aluno4} passou!!")
   aprovados +=1
else:
   print(f"O aluno: {aluno4} não passou !!!")
   reprovados +=1



print("Nome: ", alunos["aluno5"])
print("Idade: ", alunos["idade5"])
print("Nota: ", alunos["nota5"])

if nota5 >= 7:
   print(f"O aluno: {aluno5} passou!!")
   aprovados +=1
else:
   print(f"O aluno: {aluno5} não passou !!!")
   reprovados +=1





print(f"O número de Aprovados: {aprovados}")
print(f"O número de Reprovados: {reprovados}")




print(f"A media final da sua turma foi: {media}")
if media >= 7:
   print("A turma Passou!!")
else:
   print("A turma não Passou!!")