marcos = {
  "Nome": "Marcos Levy de Freitas Coelho",
  "profissão": "Programador Full Stack",
  "idade": 26,
  "Cidade": "São Luís"
}

print(marcos)
print(marcos["idade"])

for chave, valor in marcos.items():
     print(chave, ":", valor)


aluno = {
     "nome": "Marcos",
     "notas": [8, 9, 10]
}    

print(aluno["notas"])