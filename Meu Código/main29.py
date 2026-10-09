#Crie uma função: Ela deve receber um número e retornar o dobro.

def dobrar(numero):
    resultado = numero * 2
    return resultado

resultado = dobrar(7)
print(resultado)




#Crie uma função:Ela deve receber dois números e retornar a soma.

def somar(a, b):
    resultado = a + b
    print(resultado)

somar(16, 8)
somar(14, 45)
somar(18, 3)




#Maior de Idade: verificar se é maior de idade

def verficar_idade(idade):
    if idade >= 18:
        print("Maior de Idade!")
    else:
        print("Menor de Idade!")

verficar_idade(19)



#Número positivo ou negativo: A função deve retornar:
# - "Positivo" se o número for maior que 0
# - "Negativo" se for menor que 0
# - "Zero" se for igual a 0

def verificar_numero(numero):
    if numero > 0:
        print("Numero Positivo!")
    elif numero < 0:
        print("Numero negativo!") 
    else: 
        print("Número Zero!") 

verificar_numero(7)
verificar_numero(0)
verificar_numero(-6)





#Par ou ímpar
def par_ou_impar(numero):
    if numero % 2 == 0:
        print("Número Par!")
    else:
        print("Número Ímpar!")   

par_ou_impar(2)
par_ou_impar(7)



#Função + lista: Mostrar lista

def mostrar_nomes(nomes):
    for nome in nomes:
        print(nome)

nomes = ["Marcos", "Giovanna", "Adriele", "João Pedro", "Acsa"]

mostrar_nomes(nomes)



#Contar elementos: A função deve receber uma lista e retornar a quantidade de elementos.

def quantidade_elementos(lista):
    contador = 0

    for elemento in lista:
        contador += 1

    return contador

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]    
resultado = quantidade_elementos(numeros)
print(resultado)





#Somar lista 
def somar_lista(numeros):
    total = 0

    for numero in numeros:
        total = total + numero

    return total

lista = [10, 20, 30, 40]
resultado = somar_lista(lista)
print(resultado)

    