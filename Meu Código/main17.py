# Exercício 3 - Estoque

# Crie um dicionário:

# {
#     "Arroz": 10,
#     "Feijão": 5,
#     "Óleo": 3,
#     "Macarrão": 15
# }

# O usuário escolhe um produto.

# Depois informa a quantidade.

# Exemplo:

# Produto: Óleo

# Quantidade: 2

# O estoque deve diminuir.

# Resultado:

# Restam 1 unidades de Óleo

# Se não houver estoque suficiente:

# Quantidade indisponível.


print("ESTOQUE")


estoque = {
  "arroz": 10,
  "açúca": 5,
  "leite": 8,
  "feijão": 5,
  "oléo": 13,
  "sal": 6,
  "cuscuz": 10,
  "biscoito": 15,
  "macarrão": 5
}

produto = input("Produto: ").lower()

if produto in estoque:
    quantidade = int(input("Quantidade: "))

    if quantidade <= estoque[produto]:
        estoque[produto] -= quantidade
        print(f"Restam {estoque[produto]} unidades de {produto.capitalize()}")
    else:
        print("Quantidade indisponível.")
else:
   print("Produto não Encontrado>")
