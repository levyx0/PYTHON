#Percorra um dicionário usando items() e imprima cada chave e seu valor.
pessoa = {
  "nome": "maylanne Abreu",
  "idade": 19,
  "profissão": "Dentista"
}

for chave, valor in pessoa.items():
   print(chave,valor)