                                       #RELEBRANDO ATÈ AQUI OS MEUS ESTUDOS



# #For
# nomes = ["Marcos", "Paulo", "Samuel"]

# for nome in nomes:
#     print(nome)


# #for com dicionário

# programador = {
#     "nome": "Marcos",
#     "idade": 26,
#     "profissão": "Programador",
#     "salário": 5000
# } 

# for chave in programador:
#     print(chave)



# #Usando if dentro do for
# for numero in range(1,6):
#     if numero % 2 == 0:
#         print(numero)   



# #break
# # interrope o laço imediatamente.

# for i in range(20):
#     if i == 15:
#         break
#     print(i) 





    #Exercicios de for 
    #Crie um dicionário com nome, idade e cidade e imprima cada chave e seu valor usando items().


# pessoa = {
#   "nome": "Marcos Levy",
#   "cidade": "São Luis",
#   "profissão": "Programador",
#   "salário": 6000
# }

# for chave, valor in pessoa.items():
#     print(f" {chave}: {valor}")








#Crie um dicionário com 5 produtos e seus preços.

# produto = {
#     "arroz": 25,
#     "feijão": 18,
#     "macarrão": 10,
#     "manteiga": 12,
#     "açúcar": 6
# }

# for chave, valor in produto.items():
#     print(f" Produto: {chave.capitalize()} - R$ {valor}")



    #LISTAS

#pecorrendo uma lista.
# frutas = ["Laranja", "Melão", "Uva", "Melancia", "Banana"]

# for i in range(len(frutas)):
#     print(i, frutas[i]) 

#Exercicios de Litas
#1. Crie uma lista com 5 números e imprima cada um usando for:

# numeros = [10, 26, 38, 44, 59]
# for numero in numeros:
#     print(numero)


#2 Crie uma lista com 5 números e imprima apenas os números pares:

# numeros = [44, 23, 47, 11, 10, 36, 50, 84, 92]
# for numero in numeros:
#     if numero % 2 == 0:
#        print(numero)




#Peça ao usuário 5 números usando input() e armazene-os em uma lista.
#Calcule a soma e a média dos números da lista do exercício anterior

# num1 = float(input("Digite seu primeiro número: "))
# num2 = float(input("Digite seu segundo número: "))
# num3 = float(input("Digite seu terceiro numero: "))
# num4 = float(input("Digite seu quarto número: "))
# num5 = float(input("DIgite seu quinto número: "))

# numero = [num1, num2, num3, num4, num5]


# media = sum(numero) / len(numero)


# print(numero)
# print("Media dos numeros: ", media)


#Concatenar
# nome = "Marcos"
# sobrenome = "Levy"

# print(nome +" "+ sobrenome)



#Operações 
#exercicíos de Operações

# Peça dois números ao usuário e mostre:

# Soma
# Subtração
# Multiplicação
# Divisão

# num1 = float(input("Digite seu primeiro número: "))
# num2 = float(input("Digite seu segundo número: "))

# print("Soma: ", num1 + num2)
# print("Subtração: ", num1 - num2)
# print("Multiplicão: ", num1 * num2)
# print("Divisão: ", num1 / num2)



#Exercícios com todos os assuntos que eu já Estudei

#Exercício 1 - Maior de idade

nome = input("Me diga seu Nome: ")
idade = int(input("Me diga sua idade: "))

pessoa = {
  "nome": nome,
  "idade": idade
}

print("Nome: ", pessoa["nome"])
print("Idade :", pessoa["idade"], "Anos")

if idade >= 18:
   print("Maior de idade")

else: 
   print("Menor de Idade")   



