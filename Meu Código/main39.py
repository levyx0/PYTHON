# Crie as seguintes funções:
# somar(a, b)
# subtrair(a, b)
# multiplicar(a, b)
# dividir(a, b)
# eh_par(numero)
# calcular_media(notas)

# Requisitos:
# 1. Cada função deve receber seus parâmetros.
# 2. As funções matemáticas devem retornar os resultados.
# 3. A função eh_par() deve retornar True ou False.
# 4. A função dividir() deve verificar se o divisor é zero.
# 5. A função calcular_media() deve receber uma lista de notas e retornar a média.
# Assuntos: funções, parâmetros, return, operações, if/else, listas.

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    else:
        return a / b

def eh_par(numero):
    return numero % 2 == 0

def cacular_media(notas):
    total = 0 

    for nota in notas:
        total = total + nota

    return total / len(notas)


#testes
print(somar(10, 5))
print(subtrair(10, 5))
print(multiplicar(10, 5))
print(dividir(10, 5))
print(dividir(10, 0))
print(eh_par(7))
print(eh_par(8))
print(cacular_media([7, 8, 9]))

