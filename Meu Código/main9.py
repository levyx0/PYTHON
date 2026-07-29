# Exercício 4 - Cadastro de aluno

# Peça:

# Nome
# Nota 1
# Nota 2
# Nota 3

# Guarde em um dicionário.

# Calcule a média.

# Mostre:

# Nome: Marcos

# Média: 8.0

# Aprovado

# ou

# Reprovado


print("CADASTRO DE ALUNO")

nome = input("Diga o nome do aluno: ")
nota1 = float(input("Diga a primeira nota do aluno: "))
nota2 = float(input("Diga a segunda nota do aluno: "))
nota3 = float(input("Diga a terceira nota do aluno: "))

aluno = {
  "Nome": nome,
  "Nota_1": nota1,
  "Nota_2": nota2,
  "Nota_3": nota3
}

media = (aluno["Nota_1"] + aluno["Nota_2"] + aluno["Nota_3"]) / 3

print("Sua média final é: ", media)

if media >= 7:
   print("Você está Aprovado! Parabéns!")

elif media >= 4:
   print("Você está de Substutiva! Que pena!!")
else: 
   print("Se Fudeu!! Está REPROVADOOOOO!!!!!")

