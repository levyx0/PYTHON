numeros = [20, 30, 77, 44, 88, 190, 69, 36, 80, 98, 55, 42, 1, 89, 240, 250, 134, 176]

maiores_25 = []
maiores_50 = []

for numero in numeros:
    if numero > 25:
        maiores_25.append(numero)
    if numero > 50:
        maiores_50.append(numero)

print("Maiores que 25: ", maiores_25)
print("Maiores que 50: ", maiores_50)            