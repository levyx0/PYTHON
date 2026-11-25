# Analisador de palavras
# Fácil
# Peça ao usuário para digitar uma frase.
# Seu programa deverá:
# 1. Mostrar a frase em letras maiúsculas.
# 2. Mostrar a frase em letras minúsculas.
# 3. Contar quantos caracteres existem na frase.
# 4. Contar quantas palavras existem.
# 5. Verificar se a palavra "Python" aparece na frase.
# Assuntos: strings, variáveis, operações, if/else.

print("ANALISADOR DE PALAVRAS")

frase = input("Digite uma Frase: ")

#mostrando a frase em letras maiúsculas
print(frase.upper())

#mostrando a frase em letras minúsculas
print(frase.lower())


#Contando quantas palavras existem
print(frase.split())

#mostrando a quantidade de caracteres
print(len(frase))

if "pyhton" in frase:
    print("A palavra python aparece na frase")