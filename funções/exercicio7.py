# Média
# Crie uma função:
# calcular_media(notas)
# Ela deve receber uma lista de notas e retornar a média.
# Exemplo:
# notas = [7, 8, 9]print(calcular_media(notas))
# Resultado:
# 8.0

def calcular_media(notas):
    total = 0
    for nota in notas:
        total = total + nota

    return total / len(notas)

notas = [7, 8, 9]
print(calcular_media(notas))    