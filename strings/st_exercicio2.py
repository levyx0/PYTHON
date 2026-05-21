#  Verificador de palíndromo
# Peça uma palavra ao usuário e diga se ela é um palíndromo (lida igual de trás pra frente).
# Exemplos: "arara" → palíndromo | "python" → não é
# 💡 Dica: fatiamento [::-1] e lower()

print("Verficador de palíndromo")
#entrdada de dados
nome = input("Qual é o seu nome: ")

nome = nome.lower()

if nome == nome[::-1]:
   print("É Políndromo")
else:
   print("Não é Políndromo")   