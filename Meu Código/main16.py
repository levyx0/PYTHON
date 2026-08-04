# Cadastro de Alunos - lista de dicionários

alunos = []

print("Bem vindo ao cadastro de Aluno")
print("Por favor digite o nome de 5 alunos de sua turma e as notas deles para dizer se eles passaram ou não e a média da turma")
print()

for i in range(5):
    nome = input(f"Nome do aluno {i+1}: ")
    idade = int(input(f"Idade de {nome}: "))
    nota = float(input(f"Nota de {nome}: "))

    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }

    alunos.append(aluno)

print()
print("===== Resultado dos Alunos =====")
print()

aprovados = 0
reprovados = 0
soma_notas = 0

for aluno in alunos:
    print("Nome:", aluno["nome"])
    print("Idade:", aluno["idade"])
    print("Nota:", aluno["nota"])

    if aluno["nota"] >= 7:
        print("Situação: Aprovado")
        aprovados += 1
    else:
        print("Situação: Reprovado")
        reprovados += 1

    soma_notas += aluno["nota"]
    print()

media = soma_notas / len(alunos)

print("===== Resumo da Turma =====")
print(f"Quantidade de aprovados: {aprovados}")
print(f"Quantidade de reprovados: {reprovados}")
print(f"Média da turma: {media:.2f}")

if media >= 7:
    print("A turma passou!!")
else:
    print("A turma não passou!!")