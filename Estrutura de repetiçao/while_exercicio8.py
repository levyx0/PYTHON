#Solicite ao usuário 5 números e calcule a soma de todos eles utilizando while.

soma = 0
contador = 1 

while contador <= 5:
    numero = int(input(f"Digite o {contador}º numero: "))
    soma = soma + numero
    contador = contador + 1

print("A soma é: ", soma)    