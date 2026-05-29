# Exercício 4 — Filtro de notas
# Receba as notas de 10 alunos e separe em duas listas:
# Aprovados (nota >= 7)
# Reprovados (nota < 7)
# Exiba as duas listas e a quantidade em cada uma.
# 💡 Dica: dois append() dentro de um if/else


print("FILTRO DE NOTAS")

aprovados = []
reprovados = []

for i in range(10):
    nota = float(input(f"Digite a {i+1}ª nota do aluno: "))

    if nota >= 7:
        aprovados.append(nota)
    else:
        reprovados.append(nota)

print("Aprovados:", aprovados, "| Total:", len(aprovados))
print("Reprovados:", reprovados, "| Total:", len(reprovados))

    