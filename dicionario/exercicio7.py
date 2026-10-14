# Crie um dicionário chamado pessoa com as seguintes informações:
# - Nome: João
# - Idade: 25
# - Cidade: São Luís
# Faça o programa:
# 1. Mostrar o nome.
# 2. Mostrar a idade.
# 3. Alterar a idade para 26.
# 4. Adicionar uma chave chamada "profissao".
# 5. Mostrar o dicionário completo.

pessoa = {
  "nome":"Levy",
  "idade": 26,
  "cidade": "São Luís"
}

print(pessoa["nome"])
print(pessoa["idade"])
pessoa["idade"] = 20
pessoa["profissão"] = "Programador"

print(pessoa)