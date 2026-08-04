# Encontrando a média

# Sem usar:

# sum()

# Calcule a média.

# Ou seja, você mesmo deve fazer a soma usando for.

print("MÉDIAAAAAA")


lista = [23, 44, 56, 21, 90, 88, 72, 30]
soma = 0

for numero in lista:
    soma += numero

media = soma / len(lista)

print(f"A Soma é: {soma}")
print(f"A Média é: {media: .2f}")