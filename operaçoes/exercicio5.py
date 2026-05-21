#5. Calculadora de desconto
#Peça:
#porcentagem de desconto
#Depois calcule:
#valor do desconto
#valor final
#Fórmula do Desconto: Desconto = (porcentagem/ 100) x valor

print("Calculadora de Desconto")


valor = float(input("Digite o valor do produto: "))
porcentagem = float(input("Digite a porcentagem de desconto: "))

desconto = (porcentagem / 100) * valor

valor_final = valor - desconto

print(f"Valor do desconto: R$ {desconto}")
print(f"Valor final: R$ {valor_final}")