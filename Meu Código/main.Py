
# Declarando o que o Código faz!!
print("MÉDIA DAS NOTAS")

#variável onde armazeno as notas fornecidaspelo usuário.
nota1 = float(input("Me diga sua primeira nota: "))
nota2 = float(input("Diga sua segunda nota: "))

# calculo feito para obter a média.
media= (nota1 + nota2) / 2

#Condição para saber se o usuário passou ou não passou ou está reprovado
if media >= 7:
   print("Você esta aprovado!")

elif media >= 4:
   print("Você ficou de Recuperação!")  

else:
   print("Você foi reprovado!") 
