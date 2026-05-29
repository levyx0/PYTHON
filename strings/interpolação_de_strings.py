#Interpolação é simplesmente inserir o valor de uma variável dentro de uma string. É muito útil para criar mensagens personalizadas.

 #f-strings (Recomendado - Python 3.6+)
#É o método mais moderno e simples:

nome = "Marcos Levy"
idade = 26

print(f"Nome: {nome} Idade: {idade}")


#  Método .format()
# Mais antigo, mas ainda funciona:

print("O {} tem {} de idade." .format(nome, idade))


#  Formatação com % (Estilo C)
# O mais antigo, pouco usado hoje:

print("O %s tem %d de idade." % (nome, idade))