a = [1, 2, 3]
b = a

b.append(4)

print(a)
print(b)

print(a is b)
print(id(a) == id(b))



#Como fazer uma cópia da minha lista.

a = [1, 2, 3]
b = a.copy()

b.append(4)

print(a)
print(b)

#Fatiar = criar uma lista nova

letras = ["a", "b", "c", "d", "e"]
letras[1:3] #["b", "c"] (posição 1 e 2)
letras[:2]  #["a", "b"] (do começo até a posição 1)
letras[2:]  #["c", "d", "e"] (da posição 2 até o fim)
letras[:]   #["a", "b", "c", "d", "e"] (tudo)


#O exemplo do rgba
rgba = ["Vermelho", "Verde", "Azul", "Alf"]

rgba_correto = rgba[:]       # cria uma cópia
rgba_correto[-1] = "Alfa"    # corrige o último item (-1 = último)

print(rgba_correto)  # ["Vermelho", "Verde", "Azul", "Alfa"]
print(rgba)          # ["Vermelho", "Verde", "Azul", "Alf"]  <- original intacta


#. “Cópia rasa” (shallow copy)

#Rasa” significa que a cópia é só da lista externa. Se a lista tiver outras listas dentro, essas listas internas continuam compartilhadas:

a = [[1, 2], [3, 4]]
b = a[:]

b[0].append(99)

print(a)  # [[1, 2, 99], [3, 4]]  <- também mudou!

#Atribuição a fatias

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letras[2:5] = ['C', 'D', 'E']
# posições 2, 3 e 4 (c, d, e) foram trocadas
# ['a', 'b', 'C', 'D', 'E', 'f', 'g']

#Remover itens (substituindo por uma lista vazia):

letras[2:5] = []
# os três itens sumiram
# ['a', 'b', 'f', 'g']

#Limpar a lista inteira:
letras[:] = []
# []

#Atribuição a fatias também é possível, e isso pode até alterar o tamanho da lista ou remover todos os itens dela


letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letras

# substitui alguns valores
letras[2:5] = ['C', 'D', 'E']
letras

# agora remove-os
letras[2:5] = []
letras

# limpa a lista substituindo todos os elementos por uma lista vazia
letras[:] = []
letras



#É possível aninhar listas (criar listas contendo outras listas), por exemplo:

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x

x[0]

x[0][1]

print(x)


#Sequência de Fibonacci
#a soma de dois elementos define a próxima
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b                                                                                    

# Instruções if 
#Provavelmente  a mais conhecid