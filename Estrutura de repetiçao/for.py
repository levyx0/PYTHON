# O for é uma das estruturas de repetição mais importantes do Python. Ele permite executar um bloco de código várias vezes, percorrendo elementos de uma sequência, como listas, strings, conjuntos, dicionários e intervalos numéricos.

#Imagine que você tem uma lista com cinco frutas:

frutas = ["maçã", "banana", "uva", "laranja", "morango"]

#Você quer imprimir cada fruta na tela.
#Sem o for, poderia fazer assim:
print(frutas[0])
print(frutas[1])
print(frutas[2])
print(frutas[3])
print(frutas[4])

# Mas imagine se fossem 100 frutas. Seria trabalhoso!
# É aí que entra o for:

frutas = ["Maçã", "Uva", "Laranja", "Banana", "Morango"]
for fruta in frutas:
    print(fruta)
      