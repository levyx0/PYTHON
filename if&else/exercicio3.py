#Sistema de login 

usuario_correta = "Marcos"
senha_correta = "1234"

usuario = input("Digite o Usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_correta and senha == senha_correta:
     print("Login realizado com sucesso!")

else:
     print("Usuário ou senha incorretas!")

