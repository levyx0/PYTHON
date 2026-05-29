#  Exercício 2 — Maior e menor da lista
#  Peça ao usuário para digitar 5 números e armazene em uma lista. Ao final exiba:
#  O maior número
#  O menor número
#  A média dos números
#  A lista ordenada
# 💡 Dica: `max()`, `min()`, `sum()`, `sort()`


# 1. Cria uma lista vazia para guardar os números
numeros = []

# 2. Repete 5 vezes pedindo um número ao usuário
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)  # adiciona o número na lista

# 3. Exibe o maior e o menor
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))

# 4. Calcula e exibe a média
media = sum(numeros) / len(numeros)
print("Média:", media)

# 5. Ordena e exibe a lista
numeros.sort()
print("Lista ordenada:", numeros)

