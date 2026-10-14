#Média dos alunos

#Você tem:
# alunos = [
#     {"nome": "Ana", "notas": [8, 7, 9]},
#     {"nome": "Pedro", "notas": [5, 6, 4]},
#     {"nome": "Maria", "notas": [10, 8, 9]}
# ]

# Crie uma função calcular_media(notas) que receba uma lista de notas e retorne a média.
# Depois percorra os alunos e mostre:
# - O nome.
# - A média.
# - Se foi aprovado (média maior ou igual a 7) ou reprovado.

alunos = [
  {"nome": "Ana", "notas": [8, 7, 9]},
  {"nome": "Marcos", "notas": [5, 6, 8]},
  {"nome": "joão Pedro", "notas":[10, 6, 9]}
]

def calcular_media(notas):
    total = 0

    for nota in notas:
        total = total + nota
    return total / len(notas)

for aluno in alunos:
    media = calcular_media(aluno["notas"])

    if media >= 7:
        print(aluno["nome"], "-Media: ", media, "-Aprovado")
    else:
        print(aluno["nome"], "-Média: ", media, "-Reprovado")    
        