# Exercício 1 — Lista e operações
# Crie uma lista com os preços de cinco produtos:
# [15.50, 20.00, 8.50, 32.00, 14.00]
# Seu programa deve:
# 1. Calcular o valor total dos produtos.
# 2. Calcular o preço médio.
# 3. Mostrar quantos produtos custam mais de R$ 15,00.
# Conceitos: listas, for, if e operações matemáticas.

precos = [15.50, 20.00, 8.50, 32.00, 14.00]

total = 0
for preco in precos:
    total = total + preco

media = total / len(precos)
print(f"Total: R$ {total:.2f}") 
print(f"Preço médio: R$ {media:.2f}")

contador = 0
for preco in precos:
    if preco > 15:
        contador = contador + 1

print(f"Produtos que custam mais de R$ 15,00: {contador}")









# Exercício 2 — Números pares e ímpares
# Crie uma lista com os números de 1 a 20.
# Seu programa deve percorrer a lista e separar os números em duas listas: uma de pares e outra de ímpares.
# No final, mostre as duas listas e a quantidade de números em cada uma.
# Conceitos: listas, for, if/else, operador % e len().

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

pares = []
impares = []

for numero in  numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)  

print("Pares: ", pares)
print("Ímpares: ", impares)  






# Exercício 3 — Cadastro de produtos com dicionário
# Crie um dicionário que represente um produto, contendo:
# - Nome.
# - Preço.
# - Quantidade em estoque.
# Depois, calcule o valor total do estoque daquele produto e informe se é necessário repor o estoque quando a quantidade for menor que 5 unidades.
# Conceitos: dicionários, variáveis, operações e if/else.
    

produto = {
    "Nome": "Perfume",
    "Preço": 120,
    "Quantidade": 20
}

total = 0

total = produto["Preço"] * produto["Quantidade"]
print(f"O valor total do produto em estoque é: {total}")
if produto["Quantidade"] < 5:
      print("Necessário repor o estoque do produto!!")






#Removendo duplicatas

#numeros = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7]
# Seu programa deve:
# 1. Transformar a lista em um conjunto.
# 2. Mostrar os números sem duplicatas.
# 3. Mostrar quantos números únicos existem.
# 4. Verificar se o número 5 pertence ao conjunto.
# Conceitos: listas, conjuntos, len() e operador in.

numeros = [1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 3]
conjunto = set(numeros)
print(conjunto)
print(f"Quantidade de números únicos: ", len(conjunto))
if 5 in numeros:
     print("Número encontrado!")
else:
    print("Número não encontrado!")    





#Função para calcular a média
#Crie uma função chamada calcular_media que receba uma lista de notas e retorne a média.
# Depois, utilize outra parte do programa para informar a situação do aluno:
# - Média maior ou igual a 7: aprovado.
# - Média maior ou igual a 5 e menor que 7: recuperação.
# - Média menor que 5: reprovado.
# Teste a função com pelo menos três listas de notas diferentes.
# Conceitos: funções, listas, return, for ou operações matemáticas, if/elif/else.

def calcular_media(notas):
    total = 0

    for nota in notas:
        total = total + nota
    return total / len(notas) 


def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"



notas1 = [8, 7, 9]
notas2 = [5, 6, 7]
notas3 = [3, 4, 2]

for notas in [notas1, notas2, notas3]:
    media = calcular_media(notas)
    print("notas: ", notas, "-Media: ", media, "-", verificar_situacao(media))








#Controle de vendas
#Você recebeu os dados das vendas de uma loja:
# vendas = [
#     {"produto": "Perfume", "valor": 120},
#     {"produto": "Creme", "valor": 35},
#     {"produto": "Perfume", "valor": 90},
#     {"produto": "Sabonete", "valor": 12},
#     {"produto": "Creme", "valor": 45}
# ]

# Seu programa deve:
# 1. Calcular o faturamento total.
# 2. Contar quantas vendas foram registradas.
# 3. Identificar as vendas com valor superior a R$ 50.
# 4. Calcular o valor médio das vendas.
# Conceitos: listas, dicionários, for, if e operações.


vendas = [
    {"produto": "Perfume", "valor": 120},
    {"produto": "Creme", "valor": 35},
    {"produto": "Perfume", "valor": 90},
    {"produto": "Sabonete", "valor": 12},
    {"produto": "Creme", "valor": 45}
]
#faturamento total
faturamento_total = 0
for venda in vendas:
  faturamento_total = faturamento_total + venda["valor"]

#2 Quantidade de Vendas
quantidade = len(vendas)

# 3 Vendas acima de R$ 50

print("Vendas acima de R$ 50: ")
for vendas in vendas:
    if venda["valor"] > 50:
        print(venda["produto"], "-", venda["valor"])


#4 Valor Médio
media = faturamento_total / quantidade

print("\nFaturamento total: ", faturamento_total)
print("Quantidade de vendas: ", quantidade)
print("Valor médio das vendas: ", media)






#Encontrando elementos em comum
#Considere dois conjuntos de clientes:

# clientes_segunda = {"Ana", "João", "Maria", "Pedro"}
# clientes_terca = {"Maria", "Pedro", "Lucas", "Ana"}


# Seu programa deve descobrir:
# 1. Quais clientes aparecem nos dois conjuntos.
# 2. Quais clientes aparecem apenas na segunda-feira.
# 3. Quais clientes aparecem em pelo menos um dos dias.
# 4. Quantos clientes diferentes foram atendidos no total.
# Conceitos: conjuntos, operações entre conjuntos e len().


clientes_segunda = {"Ana", "João", "Maria", "Pedro"}
clientes_terca = {"Maria", "Pedro", "Lucas", "Ana"}
total = 0

#Quais clientes aparecem nos dois conjuntos.
print(clientes_segunda & clientes_terca)

#Quais clientes aparecem apenas na segunda-feira
print(clientes_segunda - clientes_terca)

#Quais clientes aparecem em pelo menos um dos dias.
print(clientes_segunda | clientes_terca)

#Quantos clientes diferentes foram atendidos no total.
total = len(clientes_segunda | clientes_terca)
print(f"Clientes diferentes atendidos: {total}")


#Função para filtrar produtos
# Crie uma função chamada filtrar_produtos que receba uma lista de dicionários contendo nome e preço.
# A função deve retornar uma nova lista contendo apenas os produtos com preço menor ou igual ao limite informado.
# Exemplo de dados:

# produtos = [
#     {"nome": "Perfume", "preco": 120},
#     {"nome": "Creme", "preco": 35},
#     {"nome": "Sabonete", "preco": 8},
#     {"nome": "Desodorante", "preco": 22}
# ]

# Ao chamar a função com o limite de R$ 30, ela deve retornar apenas o sabonete e o desodorante.
# Conceitos: funções, listas, dicionários, for, if e comparação.

produtos = [
    {"nome": "Perfume", "preco": 120},
    {"nome": "Creme", "preco": 35},
    {"nome": "Sabonete", "preco": 8},
    {"nome": "Desodorante", "preco": 22}
]


def filtrar_produtos(produtos, limite):
    filtrados = []

    for produto in produtos:
        if produto["preco"] <= limite:
            filtrados.append(produto)

    return filtrados 

resultado = filtrar_produtos(produtos, 30)
for produto in resultado:
    print(produto["nome"], "-", produto["preco"])  





#Controle de clientes devedores
# Uma loja precisa organizar os clientes que compraram parcelado.
# Utilize um dicionário em que cada chave seja o nome de um cliente e cada valor seja o total que ele ainda deve.
# Exemplo:

# dividas = {
#     "Ana": 150,
#     "João": 0,
#     "Maria": 75,
#     "Pedro": 220,
#     "Lucas": 0
# }

# Seu programa deve:
# 1. Mostrar somente os clientes que possuem dívida.
# 2. Calcular o valor total que os clientes devem à loja.
# 3. Contar quantos clientes estão devendo.
# 4. Calcular a dívida média considerando apenas os clientes devedores.
# 5. Criar uma função que receba o dicionário e retorne o total das dívidas.
# Conceitos: dicionários, for, if, funções, contagem e operações.


def total_dividas(dividas):
    total = 0

    for nome, divida in dividas.items():
        total = total + divida

    return total

dividas = {
    "Marcos": 0,
    "Adriele": 120,
    "Giovanna": 150,
    "Samilla": 100,
    "Lucas": 50
}

#Mostrar só os devedores
print("Clientes com Dívida: ")
for nome, divida in dividas.items():
    if divida > 0:
        print(nome, "-", divida)


# Total devido 
total = total_dividas(dividas)


#Contar devedores
devedores = 0
for nome, divida in dividas. items():
    if divida > 0:
        devedores = devedores + 1


#Divida média dos devedores
media = total / devedores

print("\nTotal devido: ", total)
print("Clientes devendo: ", devedores)
print("Dívida média dos devedores: ", media)









# Sistema de estoque
# Você deve criar um programa para gerenciar os produtos de uma loja.
# Comece com este dicionário:
# estoque = {    "perfume": {"preco": 120, "quantidade": 4},    "creme": {"preco": 35, "quantidade": 10},    "sabonete": {"preco": 8, "quantidade": 20}}



# Seu programa deve:
# 1. Exibir os produtos com menos de 5 unidades.
# 2. Calcular o valor total do estoque.
# 3. Criar uma função que receba o estoque e calcule seu valor total.
# 4. Permitir verificar se um produto existe no estoque.
# 5. Se o produto existir, verificar se há unidades suficientes para uma venda de quantidade informada.
# 6. Se houver estoque suficiente, calcular o valor da venda.
# Conceitos: todos os assuntos desta lista.

def valor_total_estoque(estoque):
    total = 0

    for nome, dados in estoque.items():
        total = total + dados["preco"] * dados["quantidade"]

    return total

estoque = {
    "perfume": {"preco": 120, "quantidade": 4},
    "creme": {"preco": 35, "quantidade": 10},
    "sabonete": {"preco": 8, "quantidade": 20}
}

# 1. Produtos com menos de 5 unidades
print("Produtos com menos de 5 unidades:")
for nome, dados in estoque.items():
    if dados["quantidade"] < 5:
        print(nome, "-", dados["quantidade"], "unidades")

# 2 e 3. Valor total do estoque
print("\nValor total do estoque:", valor_total_estoque(estoque))

# 4, 5 e 6. Venda
nome = input("\nQual produto deseja vender? ")

if nome in estoque:
    quantidade = int(input("Quantidade: "))

    if quantidade <= estoque[nome]["quantidade"]:
        valor = estoque[nome]["preco"] * quantidade
        print(f"Venda realizada! Valor: R$ {valor}")
    else:
        print("Estoque insuficiente. Disponível:", estoque[nome]["quantidade"])
else:
    print("Produto não encontrado!")