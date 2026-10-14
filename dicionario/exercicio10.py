#Cadastro de vários alunos
#Crie uma lista de dicionários:

# alunos = [
#     {"nome": "Ana", "nota": 8},
#     {"nome": "Pedro", "nota": 5},
#     {"nome": "Maria", "nota": 9},
#     {"nome": "Lucas", "nota": 6}
# ]

# Percorra a lista e mostre o nome de cada aluno e sua situação:
# - Nota maior ou igual a 7: aprovado.
# - Nota menor que 7: reprovado.

alunos = [
  {"nome": "Ana", "nota": 8},
  {"nome": "Marcos", "nota": 5},
  {"nome": "Maria", "nota": 9},
  {"nome": "Lucas", "nota": 6}
]

for aluno in alunos:
    if aluno["nota"] >= 7:
        print(aluno["nome"], "-Aprovado")
    else:
        print(aluno["nome"], "-reprovado")    
