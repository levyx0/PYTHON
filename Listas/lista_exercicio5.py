# Exercício 5 — Jogo de par ou ímpar
# Crie uma lista com 10 números aleatórios entre 1 e 100. Separe em duas listas: pares e ímpares. Exiba as duas listas e a soma de cada uma.
# 💡 Dica: import random, random.randint(), operador %

import random #importa uma biblioteca de números aleatórios
#cria uma lista com 10 número aleatórios
numeros = []

for i in range(10):
    numero = random.randint(1, 100)#sorteia um número entre 1 e 100
    numeros.append(numero)


#Cria as duas litas
impares = []
pares = []


#separa os números
for numero in numeros:
    if numero % 2 == 0: #se o resto da divisão por 2 for 0  é par
        pares.append(numero)
    else:
        impares.append(numero)

#Exibe o resultados
print("Números Gerados: ", numeros)   
print("Números Pares: ", pares, "| Soma: ", sum(pares))
print("Números Ímpares: ", impares, "| Soma: ",sum(impares))    

