#Rersumo da Linguagem python

#listas: Uma lista é uma estrutura usada para guardar vários valores dentro de uma única variável.

#Alterando elementos
frutas = ["maçã", "banana", "laranja"]
frutas[1] = "morango"

print(frutas)


#Adcionando elementos
#Existem várias formas.
#APPEND() método mais usado no começo

loja = ["feijão", "arroz"]
loja.append("açúcar")
print(loja)
#O append() adciona no final da lista.

#Removendo Elementos
#remove()

frutas = ["pêra", "abacate", "laranja"]
frutas.remove("abacate")
print(frutas)
#remove procura o valor que eu informei.


#Remover pela posição
#também pode usar pop().

farmacia = ["Ibuprofeno", "Shampoo", "Desodorante"]
farmacia.pop(0)
print(farmacia)
#Estamos dizendo, remova o elemento no índice 0.



#Descobrir o tamanho da lista
#Usamos len():

materia_de_construção = ["cimento", "tijolo", "argamassa", "brita", "telha", "prego", "piso" ]
print(len(materia_de_construção))
#Isso significa que existem 7 elementos na lista.


#Pecorrendo uma lista com for.

nomes = ["João Pedro", "Gian", "Marcos", "Paulo Henrique", "Samuel", "Giovanna"]

for nome in nomes:
    print(nome)

#Para cada elemento dentro de nomes, coloque esse elemento na variável nome e execute o código.

#Lista + if

notas = [8, 10, 6, 7, 2, 8, 9, 10]

for nota in notas:
    if nota >= 7:
        print(nota)

#Aqui ja estamos começando a juntar conceitos. isoo é muito importante para começar a pensar como programador.


#Verificar se algo está na lista

igreja = ["pastor", "diácono", "obreiro", "músico", "dirigente"]

if "obreiro" in igreja:
    print("Obreiro está na lista!!")


#Exemplo:
usuarios = ["Giovanna", "Adriele", "Marcos", "Acsa"]

nome = input("Digite seu nome: ")

if nome in usuarios:
    print("Usuário encontrado!")
else:
    print("Usuário não encontrado!!")  

#Aqui já temos um pequeno programa.  



#Fatiamento : pegar uma parte da lista.
#tambem pode pegar um pedaço da lista.

numeros = [10, 20, 30, 40, 50, 60]

print(numeros[1:4])

#resultado : [20, 30, 40]
#lógica é : [10, 20, 30, 40, 50, 60]
#                1          4  
# O índice inicial entra, mas o final não entra.




# Alguns métodos importantes
# Append()         adciona no final
# remove()         remove um valor
# pop()            remove por índice
# sort()           ordena
# reverse()        inverte
# count()          conta ocorrências
# index()          encontra a posição
# clear()          limpa a lista 




#exercício
# Faça um programa que:

# Mostre todos os produtos.
# Pergunte ao usuário qual produto ele quer procurar.
# Verifique se o produto está na lista.
# Se estiver, mostre "Produto encontrado".
# Caso contrário, mostre "Produto não encontrado".

# Depois podemos subir um nível e fazer listas + funções + dicionários, que é justamente onde as coisas começam a ficar mais próximas de um sistema real, como o software da loja que você quer desenvolver.



produtos = ["perfume", "sabonete", "shampoo", "creme"]

for produto in produtos:
    print(produto)

escolha = input("Qual produto da lista você deseja: ")

if escolha in produtos:
    print("Produto encontrado!!!")
else:
    print("Produto não encontrado!!!")    

