# Contador de números positivos e negativos
# Solicite números ao usuário até que ele digite zero.
# No final, mostre:
# - Quantos números positivos foram digitados.
# - Quantos números negativos foram digitados.

positivos = 0
negativos = 0

numero = int(input("Digite um número (0 para encerrar): "))

while numero != 0:
    if numero > 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1
    numero = int(input("Digite um número (0 para encerrar)"))   

print("Positivos: ", positivos)
print("Negativos: ", negativos)