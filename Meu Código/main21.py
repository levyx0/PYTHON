#ESTUDOS
#exercícios

lista = [2, 4, 5, 8, 13, 6, 11, 23, 67, 865, 9]

def verificar_numeros(listas):
    for numero in lista:
        if numero % 2 == 0:
            print(numero, "Par")
        else:
            print(numero, "Ímpar") 


verificar_numeros(lista)






#crie um dicionário representando um aluno

aluno = {
    "nome": "Carlos",
    "idade": 20,
    "nota": 10
}

def verificar_aluno(aluno):
    nota = aluno["nota"]

    if nota >=7:
        print("Aprovado")
    elif nota >= 5 and nota <= 6.9:
        print("Recuperação")
    else:
        print("Reprovado")   


verificar_aluno(aluno)




#Crie uma lista com números repetidos

numeros = [1, 2, 2, 3, 2, 4, 5, 1, 6, 3, 7, 2, 8]


def analizar_numeros(numeros):
    conjunto = set(numeros)
    print("Litra Original: ", numeros)
    print("Conjunto sem repetição: ", conjunto)
    print("Quantidade de números diferentes: ", len(conjunto))


analizar_numeros(numeros)







#Crie uma lista contendo 5 dicionários de produto
#Crie uma função verificar_produtos(produtos).
#Para cada produto:
#Se o preço for maior que 50, mostre "Produto caro"
#Caso contrário, mostre "Produto barato"

produtos = [
    {"nome": "Perfume", "preço": 150},
    {"nome": "Sabonete", "preço": 25},
    {"nome": "Hidratante","preço": 40},
    {"nome": "Kit Malbeck", "preço": 200},
    {"nome": "Colônia Bebê", "preço": 20}
]


def verficar_produtos(produtos):
    for produto in produtos:
        if produto["preço"] > 50:
            print("Produto Caro!!!") 
        else:
            print("Produto Barato!!!!!")   

verficar_produtos(produtos)  







# Você possui duas listas:

# clientes_loja1 = ["João", "Maria", "Carlos", "Ana"]
# clientes_loja2 = ["Carlos", "Ana", "Pedro", "Lucas"]

# Crie uma função que descubra:

# Quais clientes estão nas duas lojas
# Quais clientes estão somente na loja 1
# Quais clientes estão somente na loja 2
# Todos os clientes, sem repetição

# Dica: transforme as listas em set.


clientes_loja1 = ["João", "Marcos", "Gardênia", "Giovanna",]
clientes_loja2 = ["Carlos", "Giovanna", "Marcos", "Lucas"]

def analisar_clientes(lista1, lista2):
    loja1 = set(lista1)
    loja2 = set(lista2)

    print("Nas duas lojas: ", loja1 & loja2)
    print("Somente na Loja 1: ", loja1 - loja2)
    print("Somente na loja 2: ", loja2 - loja1)
    print("Todos os clientes: ", loja1 | loja2)

analisar_clientes(clientes_loja1, clientes_loja2)








# Crie um dicionário com alunos e suas notas:
# alunos = {
#     "João": 8,
#     "Maria": 5,
#     "Carlos": 9,
#     "Ana": 6
# }
# Crie uma função que percorra o dicionário e crie três listas:
# aprovados
# recuperacao
# reprovados
# Regras:
# >= 7 → aprovado
# >= 5 e < 7 → recuperação
# < 5 → reprovado

alunos = {
    "João": 8,
    "Marcos": 10,
    "Giovanna": 9,
    "Lucas": 6,
    "Samylla": 4
}

def classificar_alunos(alunos):
    aprovados = []
    recuperacao = []
    reprovados = []

    for nome, nota in alunos.items():
        if nota >= 7:
            aprovados.append(nome)
        elif nota >= 5:
            recuperacao.append(nome)
        else:
            reprovados.append(nome)        






