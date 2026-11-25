# Cadastro e análise de alunos
# Intermediário
# Crie um programa que cadastre 5 alunos e suas notas em um dicionário.
# Exemplo:
# alunos = {
#     "Ana": 8.5,
#     "João": 6.0,
#     "Maria": 9.0
# } 

# Seu programa deverá:
# 1. Mostrar o nome e a nota de cada aluno.
# 2. Calcular a média geral da turma.
# 3. Identificar os alunos aprovados (média maior ou igual a 7).
# 4. Identificar os alunos reprovados (média menor que 5).
# 5. Mostrar os alunos em recuperação (média entre 5 e 6.9).
# Assuntos: dicionários, operações, for, if/else, variáveis.

print("Cadastro e Análise de Alunos")
#Cadastro de Alunos.
aluno1 = input("Cadastre o nome do primeiro aluno: ")
nota1 = float(input(f"Informe a nota do {aluno1}: "))

aluno2 = input("Cadastre o nome do segundo aluno: ")
nota2 = float(input(f"Informe a nota do {aluno2}: "))

aluno3 = input("Cadastre o nome do terceiro aluno: ")
nota3 = float(input(f"informe a nota do {aluno3}: "))

aluno4 = input("Cadastre o nome do quarto aluno: ")
nota4 = float(input(f"Informe a nota do {aluno4}: "))

aluno5 = input("Cadastre o nome do quinto aluno: ")
nota5 = float(input(f"Informe a nota do {aluno5}: "))


turma = {

aluno1: nota1,
aluno2: nota2,
aluno3: nota3,
aluno4: nota4,
aluno5: nota5
}


#Nome e Nota de cada aluno
print("\nAluno e notas: ")
for nome, nota in turma.items():
    print(nome, "-", nota)


#Média geral da turma
total = 0
for nome, nota in turma.items():
    total = total + nota

media = total / len(turma)

#Verficando alunos reprovados, aprovados e em recuperação.
aprovados = []
recuperacao = []
reprovados = []

for  nome, nota in turma.items():
     if nota >= 7:
         aprovados.append(nome)
     elif nota >= 5:
         recuperacao.append(nome)
     else:
         reprovados.append(nome)  

print("\nMedia geral da turma: ",media) 
print("Alunos Aprovados: ", aprovados) 
print("Alunos em Recuperação: ", recuperacao)
print("Alunos Reprovados: ", reprovados)                        





    

