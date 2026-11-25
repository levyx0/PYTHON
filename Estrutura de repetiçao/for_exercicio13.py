#Soma dos ímpares: crie uma estrutura que percorra os números de 1 até 100 e calcule a soma de todos os números ímpares.
soma = 0
for numero in range(1, 101):
    if numero % 2 != 0:
        soma += numero

print("Soma dos ímpares de 1 a 100: ", soma)
    
    