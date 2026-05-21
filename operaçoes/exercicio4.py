#4. Comparador de números
#Peça dois números e mostre:
#se são iguais
#qual é maior
#qual é menor

print("Comparador de Números")

num1 = int(input("Digite seu primeiro número: "))
num2 = int(input("Digite seu segundo número: "))

if num1 == num2 :
  print("Os Números sao iguais")

elif num1 > num2:
    print(f"{num1} é maior")
    print(f"{num2} é menor")

else:
    print(f"{num2} é maior")
    print(f"{num1} é menor")