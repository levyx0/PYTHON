# — Limpador de cadastro
#O usuário digita o nome e o email. Seu programa deve:
# #Remover espaços extras do nome e email
#Deixar o nome com a primeira letra de cada palavra maiúscula
#Deixar o email todo em minúsculo
#Exibir os dados "limpos"
#Dica: strip(), title(), lower()

print("LIMPADOR DE CADASTRO")
#Entrada de Dados
nome = input("Digite seu Nome: ")
email = input("DIgite seu email: ")

#Limpandos Dados
nome_limpo = nome.strip().title()
email_limpo = email.strip().lower()

#Exibindo Resultados
print("\nDados seu nome: ")
print("Nome: ", nome_limpo)
print("Email: ", email_limpo)