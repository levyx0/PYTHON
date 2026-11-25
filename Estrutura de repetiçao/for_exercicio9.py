#Crie uma variável com uma palavra. Utilize for para contar quantas vogais existem nela.

palavra = "Programador"
vogais = 0

for letra in palavra:
    if letra in "aeiou":
        vogais += 1
print(f"A palavra {palavra} tem {vogais} vogais.")        