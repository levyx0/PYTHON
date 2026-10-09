#Funções
#Uma função é um bloco de código que executa uma determinada tarefa.

# Imagine que você precisa calcular a média de um aluno várias vezes.
# Sem função

# nota1 = 8
# nota2 = 7

# media = (nota1 + nota2) / 2
# print(media)

# nota1 = 10
# nota2 = 9

# media = (nota1 + nota2) / 2
# print(media)

# Estamos repetindo código.
# Com uma função, podemos criar a lógica uma vez e reutilizá-la:

# def calcular_media(nota1, nota2):
#     media = (nota1 + nota2) / 2
#     print(media)
#Agora podemos chamar:

# calcular_media(8, 7)
# calcular_media(10, 9)


#Criando uma função

def saudacao():
    print("Olá!")

#função criada, mas não executada, para executar.

saudacao()

#Função com parâmetros
#Podemos mandar informações para a função.

def saudacao(nome):
    print("Olá", nome)

saudacao("Marcos")
saudacao("Adriele")
saudacao("Giovana")

#nome é um parâmetro.
#"Marcos" é o argumento passado para função.

#Parâmetro = espaço reservado para receber uma informação.


#Vários parâmetros
#Uma função pode receber várias informações:

def somar(a, b):
    resultado = a + b
    print(resultado)

somar(16, 8)


#return — MUITO importante

def diminuir(a, b):
    resultado = a - b
    return resultado

resultado = diminuir(10, 5)
print(resultado)

#O return devolve um valor para quem chamou a função

#print x return

#com print:

def multiplicação(a, b):
    print(a * b)


def multiplicacao(a, b):
    return a * b



#Função com if/else

def verificar_idade(idade):
    if idade >= 18:
        return "Maior de Idade"
    else:
        return "Menor de Idade"


resultado = verificar_idade(75)
print(resultado)


#Função com lista

def mostra_frutas(frutas):
    for fruta in frutas:
        print(fruta)

frutas = ["Maçã", "Manga", "Abacate"]
mostra_frutas(frutas)




#Função que trabalha com uma lista

def contar_numeros(numeros):
    contador = 0

    for numero in numeros:
        contador += 1

    return contador    


lista = [10, 20, 30, 40]
quantidade = contar_numeros(lista)
print(quantidade)




#Exemplo
produtos = ["perfume", "shampoo", "sabonete"]

def procurar_produto(produtos, produto):
    if produto in produtos:
        return "Produto Encontrado"
    else:
        return "Produto não Encontrado"

resultado = procurar_produto(produtos, "perfume")

print(resultado)
    