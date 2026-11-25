#Duas turmas participaram de atividades
# turma_a = {"Ana", "João", "Maria"}
# turma_b = {"João", "Pedro", "Ana", "Lucas"}

# 1. Crie um conjunto com todos os alunos das duas turmas, sem duplicatas.
# 2. Conte quantos alunos diferentes participaram.
# 3. Exiba o resultado.
# Conceito: união (|).

turma_a = {"Ana", "João", "Maria"}
turma_b = {"João", "Pedro", "Ana", "Lucas"}

print(turma_a | turma_b)

print(len(turma_a | turma_b))