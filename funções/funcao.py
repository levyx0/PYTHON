# O que é uma função? Uma função é um bloco de código que realiza uma tarefa específica.

#Como cria uma função em python
def saudacao():
    print("Olá mundo!!")

#chamando a função
#criar a função não faz ela executar
saudacao()

#Funções com Parâmetros
def saudacao(nome):
    print(f"Olá, {nome}")

saudacao("Marcos")
saudacao("Paulo")
saudacao("Gardênia")

#mais de um parâmetro
def soma(a, b):
    print(a + b)

soma(23, 45)

#O comando Return
#Às vezes queremos devolver um valor.

def soma(a, b):
    return a + b

resultado = soma(10, 40)
print(resultado)





#calcular Média
def calcular_media(n1, n2, n3):
    return(n1 + n2 +n3) / 3

media = calcular_media(7, 9, 10)
print(media)




#Usando if com funções
def verificar_idade(idade):

    if idade >= 18:
        print("Maior de idade")
    else:
        print("Menor de idade")


verificar_idade(15)    




#funções podem usar listas
def mostra_lista(lista):

    for item in lista:
        print(item)

frutas = ["Maçã", "Banana", "Abacaxi", "Uva", "Abacate", "Melão"]
mostra_lista(frutas)


#funções podem usar dicionários
def mostrar_produtos(produtos):

    for nome, preco in produtos.items():
        print(f"{nome}: R$ {preco}")

produtos = {
    "Arroz": 20,
    "Açucar": 15,
    "Oléo": 10,
    "Manteiga": 12,
    "Feijão": 15
}   
mostrar_produtos(produtos)    


#Resusmo
#Criar função:      def nome():
#Executar função:   nome()
#Receber informações:   def soma(a, b)
#Devolver resultado:    return
#Mostrar Resultado:  print()


#EXERCÍCIOS:

#Crie uma função chamada saudacao() que imprima: Bem-vindo ao sistema!

def saudacao():
    print("Bem vindo ao sistema!")

saudacao()    



#Crie uma função chamada mostrar_nome(nome) que receba um nome e imprima: Olá, Marcos!

def mostrar_nome(nome):
    print(f"Olá, {nome}")

mostrar_nome("Marcos")
mostrar_nome("Giovanna")
mostrar_nome("Gardênia")    


#Crie uma função chamada somar(a, b) que receba dois números e retorne a soma usando return.
def somar(a, b):
    return a + b

resultado = somar(25, 36)
print(resultado)




#Crie uma função chamada par_ou_impar(numero) que informe se o número é par ou ímpar
def par_ou_impar(numero):
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar") 

par_ou_impar(28)        




#Crie uma função chamada calcular_media(n1, n2, n3) que retorne a média de três notas.
def calcular_media(n1, n2, n3):
    return(n1 + n2 + n3) / 3

media = calcular_media(7, 8, 8)
print(media)    