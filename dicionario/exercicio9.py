#Percorrendo um dicionário
#Você tem:
# aluno = {
#     "nome": "Carlos",
#     "matematica": 8,
#     "portugues": 6,
#     "ciencias": 9
# }
# Use um for para percorrer as informações e mostrar todas as chaves e valores.
# Depois, mostre somente as notas maiores ou iguais a 7.
# Conteúdos: dicionários, for e if.


aluno = {
  "nome": "Carlos",
  "matematica": 8,
  "portugues": 6,
  "ciencias": 9
}
print("Todas as informações: ")
for chave, valor in aluno.items():
    print(chave, ":", valor)

print("\nNotas maiores ou iguais a 7: ")
for chave, valor in aluno.items():
    if chave != "nome" and valor >= 7:
        print(chave, ":", valor)