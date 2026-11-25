#Utilize while para imprimir todos os números pares entre 1 e 50.

numero = 1

#opcao 1
while numero <= 50:
    if numero % 2 == 0:
        print(numero)
    numero = numero + 1    

#opção 2
numero = 2
while numero <= 50:
    print(numero, end=" ")
    numero += 2    