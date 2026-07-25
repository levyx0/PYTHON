#Crie um dicionário chamado aluno com uma lista de três notas. Calcule e imprima a média dessas notas.

aluno = {
  "nome": "Marcos Levy",
  "nota1": 8,
  "nota2": 6,
  "nota3": 10
}

media = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"]) / 3
print("O aluno", aluno["nome"], "tem a média: ", media)