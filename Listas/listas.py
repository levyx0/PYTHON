frutas = ["Maçã", "Uva", "Laranja", "Melão", "Melancia"]
for indice, fruta in enumerate(frutas):
    print(indice, "-", fruta)



frutas = ["Maçã", "Uva", "Laranja", "Melão", "Melancia"]
frutas.append("Mamão")
frutas.insert(0, "Morango")
frutas.extend(["kiwi", "Goiaba"])
print(frutas)

    


quadrados = []
for i in range(1, 11):
    quadrados.append(i * 2)
print(quadrados)




numeros = [3, 1, 5, 10, 8, 9, 2, 4]
numeros. sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

print(len(numeros))
numeros.copy
print(numeros)



matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()    
