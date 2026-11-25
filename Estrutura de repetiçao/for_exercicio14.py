#Contagem de letras: crie uma variável com uma frase. Utilize for para contar quantas vezes a letra "a" aparece nela.

frase = "Eu amo estudar Programação."
total = 0

for letra in frase.lower():
    if letra in "aáàâã":
        total += 1

print(f'A letra "a" aparece {total} vezes.')
        