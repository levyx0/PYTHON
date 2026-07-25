#Faça um programa que pergunte o nome e a idade de uma pessoa, armazene esses dados em um dicionário e depois exiba uma mensagem como: Nome: Levy
#Idade: 25 anos

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

pessoa = {
  "nome": nome,
  "idade": idade
}

print("Nome: ", pessoa["nome"])
print("Idade: ",pessoa["idade"], "anos")





