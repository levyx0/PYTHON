# 1. Análise de números
# Fácil

# Crie um programa que receba 10 números do usuário e armazene-os em uma lista.

# Depois, o programa deverá:
# 1. Mostrar todos os números.
# 2. Calcular a soma dos números.
# 3. Calcular a média.
# 4. Identificar os números pares e ímpares.
# 5. Mostrar o maior e o menor número.
# Assuntos: variáveis, listas, operações, if/else, for.

print("ANÁLISE DE NÚMEROS")

numeros = []

#Fazendo a pergunta ao usuário e usando for para imprimir 10 vezes e adcionando a uma lista
for i in range(10):
    numero = float(input(f"Digite um número {i + 1}: "))
    numeros.append(numero)

#criando uma variavel para acumular os  números e somar os números
total = 0
for numero in numeros:
    total = total + numero


#Calculando a Média dos Números.
media = total / len(numeros)

#variaveis para guardar números pares e ímpares
pares = []
impares = []

#verificando se um numero é par ou ímpar!
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)    


#criando variáveis para guardar o menor número e o maior número.
maior = numeros[0]
menor = numeros[0]

#verificando qual o número é menor e maior.
for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero    


#printando os resultados
print("Números digitados: ", numeros)
print("Soma dos números: ", total)
print("Média dos números: ", media)
print("Números Pares: ", pares)
print("Números ímpares: ", impares)
print("Maior Número: ", maior)
print("Menor Número: ", menor)


