 #Um dicionário é uma coleção que armazena dados no formato: chave → valor

#Criando um dicionário
pessoa = {
    "nome": "Marcos Levy",
    "idade": 26,
    "cidade": "São Luís"
}

print(pessoa)

#Acessando Valores
#Em um dicionário usamos a chave.
pessoa = {
  "nome": "Giovana",
  "idade": 24,
  "cidade": "São Luis"
}

print(pessoa ["idade"])


#Alterando valores
pessoa = {
  "nome": "Giovana",
  "idade": 24,
}

pessoa["idade"] = 26

print(pessoa ["idade"])

#Adicionando novos itens
#Se a chave não existir, ela será criada.

pessoa = {
  "nome": "Levy"
}

pessoa["profissão"] = "Juiz"
print(pessoa)

#Removendo itens
#utilizando del

pessoa = {
  "nome": "Marcos",
  "idade": 25
}

del pessoa["idade"]
print(pessoa)

#pecorrendo um dicionário
#apenas as chaves
pessoa = {
  "nome": "Eliezer Pamonha",
  "idade": 21,
  "profissão": "Dentista"
}

for chave in pessoa:
    print(chave)


#pecorrendo um dicionário
#Apenas os Valores

pessoa = {
    "nome": "Eliezer Pamonha",
    "idade": 21,
    "profissão": "Dentista"
}

for valor in pessoa.values():
     print(valor)


#pecorrendo um dicionário
#chaves e valores
pessoa = {
     "nome": "ELiezer Pamonha",
     "idade": 21,
     "profissão": "Dentista"
}

for chave, valor in pessoa.items():
     print(chave,valor)


#Verificando se uma chave existe
pessoa = {
     "nome": "Levy",
     "idade": 25
}   

if "nome" in pessoa:
     print("Existe!")



#Utilizando o metodo get()

pessoa = {
     "nome": "Levy"
}

print(pessoa["idade"])
#Isso gera um erro: KeyError: 'idade'

#Uma forma mais segura é usar get(): print(pessoa.get("idade"))
#Resultado:none!

pessoa = {
     "nome": "Levy"
}
print(pessoa.get("idade"))


#Dicionários podem guardar vários tipos de dados
pessoa = {
     "nome": "Levy",
     "idade": 25,
     "altura": 1.78,
     "casado": False  
}

#Dicionário com Listas

aluno = {
     "nome": "Carlos",
     "notas": [8, 9, 10]
}

print(aluno["notas"])

#Podemos acessar um elemento da lista: print(aluno["notas"][0])



#Dicionários dentro de Dicionários:

pessoa = {
     "nome": "Levy",
     "endereço": {
          "cidade": "São Luís",
          "estado": "MA"
     }
}

print(pessoa["endereço"]["cidade"])




#Exemplo:

funcionario = {
     "nome": "Marcos",
     "idade": 26,
     "Cargo": "Desenvolvedor de Software",
     "salario": 6500
}

print("Nome: ", funcionario["nome"])
print("Idade: ", funcionario["idade"])
print("Cargo: ", funcionario["Cargo"])
print("Salário: ", funcionario["salario"])
