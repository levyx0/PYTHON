# Exercício 6 — Aprovados

# Você tem:

# notas = [8, 5, 7, 3, 9, 6]

# Percorra a lista.

# Para cada nota:

# >= 7 → "Aprovado"
# < 7 → "Reprovado"

# Exemplo esperado:

# 8 - Aprovado
# 5 - Reprovado
# 7 - Aprovado


notas = [8, 4, 1, 0, 5, 9, 6, 3, 10]

aprovados = []
reprovados = []
recuperacao = []

for nota in notas:
     if nota >= 7:
         aprovados.append(nota)
     elif nota >= 4:
          recuperacao.append(nota)
     else:
          reprovados.append(nota)     

print(f"Aprovados: {aprovados}")
print(f"Em recuperação: {recuperacao}")
print(f"Rprovados: {reprovados}")                  
