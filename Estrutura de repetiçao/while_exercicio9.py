# Média de notas

# Solicite notas de um aluno até que o usuário digite -1.

# Depois:
# - Calcule a média das notas.
# - Mostre quantas notas foram informadas.
# - Informe se o aluno foi aprovado (média maior ou igual a 7).

soma = 0
quantidade = 0

nota = float(input("Digite uma nota(ou -1 para enecerrar): "))

while nota != -1:
    soma = soma + nota
    quantidade = quantidade + 1
    nota = float(input("Digite uma nota(ou -1 para encerrar): "))

if quantidade == 0: 
    print("Nenhuma nota foi informada.")
else:
    media = soma / quantidade
    print("Notas informadas: ", quantidade)
    print("Média", media)

    if media >= 7:
        print("Aluno aprovado")
    else: 
        print("Aluno reprovado")    