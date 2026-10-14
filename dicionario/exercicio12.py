#Calcular preço de compra
#Crie este dicionário:

# precos = {
#     "perfume": 120,
#     "shampoo": 25,
#     "sabonete": 8
# }

# Crie uma função chamada calcular_compra(produto, quantidade).
# Ela deve:
# 1. Verificar se o produto existe.
# 2. Se existir, multiplicar o preço pela quantidade.
# 3. Retornar o valor total.
# 4. Se não existir, retornar uma mensagem informando que o produto não foi encontrado.
# Exemplo: 3 shampoos devem custar 75.


precos = {
  "perfume": 120,
  "shampoo": 25,
  "sabonete": 8
}

def calcular_compra(produto, quantidade):
    if produto in precos:
        return precos[produto] * quantidade
    else:
        return "Produto não encontrado" 

print(calcular_compra("shampoo", 3))
print(calcular_compra("perfume", 2))
print(calcular_compra("tênis", 1))       