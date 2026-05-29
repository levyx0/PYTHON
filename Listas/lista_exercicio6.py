# Exercício 1 — Cadastro de alunos
# Crie um programa que cadastra 5 alunos com nome e idade. Ao final exiba:
# A lista de alunos com suas idades
# O aluno mais velho
# O aluno mais novo
# 💡 Dica: duas listas, uma para nomes e outra para idades. max(), min(), index()

print("CADASTRO DE ALUNO")

nomes = []
idades = []

for i in range(5):
    nome = input(f"Digite o nome do {i + 1} aluno: ")
    idade = int(input(f"Digite a idade do {nome}: "))
    nomes.append(nome) #adciona nome na lista de nomes
    idades.append(idade) #adciona idade na lista de idades


for i, nome in enumerate(nomes):
    print(f"{i + 1} - {nome} | {idades[i]} anos")  


#Acha o mais velho
maior_idade = max(idades)     #pega a maior idade
posicao = idades.index(maior_idade) #pega a posição dela
mais_velho = nomes[posicao] #pega o nome nessa posição

#acha o mais novo
menor_idade = min(idades)  #pega a menor idade
posicao = idades.index(menor_idade) # pega a posição dela
mais_novo = nomes[posicao] #pega o nome nessa posição

print(f"Mais velho: {mais_velho} | {maior_idade} anos")
print(f"Mais novo: {mais_novo} | {menor_idade} anos")

