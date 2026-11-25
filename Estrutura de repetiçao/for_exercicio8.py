#Crie uma lista com 10 números. Utilize for e if para contar quantos são maiores que 15.

numeros = [10, 24, 6, 16, 7, 34, 45, 88, 32, 2]
maior_que_15 = 0

for numero in numeros:
    if numero > 15:
       maior_que_15 += 1

print(maior_que_15)