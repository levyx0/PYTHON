#Crie uma lista com 5 notas. Utilize for para calcular a média dos valores.

notas = [7, 8, 6, 9, 10]
soma = 0

for nota in notas:
    soma += nota

media = soma / len(notas)
print("Média: ", media)
    