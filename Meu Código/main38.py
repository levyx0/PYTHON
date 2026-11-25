# Operações com conjuntos
# Intermediário
# Duas turmas participaram de um evento.

# turma_a = {"Ana", "João", "Pedro", "Maria"}
# turma_b = {"João", "Carlos", "Maria", "Lucas"}

# Seu programa deverá:
# 1. Mostrar todos os participantes, sem duplicatas.
# 2. Identificar quem participou das duas turmas.
# 3. Identificar quem participou apenas da turma A.
# 4. Identificar quem participou apenas da turma B.
# 5. Contar o total de participantes únicos.
# Assuntos: conjuntos, operações, variáveis.

turma_a = {"Giovanna", "Lucas", "Marcos", "Levy"}
turma_b = {"Marcos", "Felipe", "Adriele", "Giovanna"}

print(f"Todos os participantes das duas turmas: {turma_a | turma_b}")
print(f"Participantes que participaram das duas turmas: {turma_a & turma_b}")

print(f"Participantes da turma a: {turma_a - turma_b}")
print(f"Participantes da turma b: {turma_b - turma_a}")

print(f"Total de participantes: {len(turma_a | turma_b)}")



