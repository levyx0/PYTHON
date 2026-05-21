

# Métodos úteis da classe strings.





nome = "oLA MUndO"

print(nome.upper())   #  # "OLÁ, MUNDO!"     → tudo maiúsculo
print(nome.lower())   # # "olá, mundo!"     → tudo minúsculo
print(nome.title())   # "Olá, Mundo!"     → primeira de cada palavra maiúscula
print(nome.capitalize()) ## "Olá, mundo!"     → só primeira letra maiúscula
print(nome.swapcase()) #  # "OLÁ, MUNDO!"     → inverte maiúsculo/minúsculo


   #Remoção de espaços
texto = "   olá   "

texto.strip()        # "olá"    → remove dos dois lados
texto.lstrip()       # "olá   " → remove só da esquerda
texto.rstrip()       # "   olá" → remove só da direita

   #Busca e verificação
texto = "Python é incrível"

texto.find("é")           # 7       → posição da primeira ocorrência (-1 se não achar)
texto.count("i")          # 2       → quantas vezes aparece
texto.startswith("Py")    # True    → começa com?
texto.endswith("vel")     # True    → termina com?
"incrível" in texto       # True    → contém?


   # Substituição e divisão
texto = "eu gosto de café"

texto.replace("café", "Python")  # "eu gosto de Python"

texto.split(" ")   # ["eu", "gosto", "de", "café"] → divide em lista
texto.split(",")   # divide pelo separador escolhido

# join → junta uma lista em string (oposto do split)
palavras = ["Python", "é", "top"]
" ".join(palavras)   # "Python é top"
"-".join(palavras)   # "Python-é-top"

 
 
   # Verificações de conteúdo

"123".isnumeric()     # True  → só números?
"abc".isalpha()       # True  → só letras?
"abc123".isalnum()    # True  → só letras e números?
"   ".isspace()       # True  → só espaços?
"Olá".islower()       # False → tudo minúsculo?
"OLÁ".isupper()       # True  → tudo maiúsculo?




# Formatação e alinhamento
"olá".center(11)         # "    olá    "  → centraliza
"olá".ljust(10)          # "olá       "  → alinha à esquerda
"olá".rjust(10)          # "       olá"  → alinha à direita
"olá".center(11, "-")    # "----olá----" → centraliza com preenchimento

# f-string (mais moderno e recomendado)
nome = "Carlos"
saldo = 1500.5
print(f"Olá, {nome}! Seu saldo é R$ {saldo:.2f}")
# "Olá, Carlos! Seu saldo é R$ 1500.50"





   # Fatiamento de strings
texto = "Python"
#        012345   → índices

texto[0]      # "P"        → primeiro caractere
texto[-1]     # "n"        → último caractere
texto[0:3]    # "Pyt"      → do índice 0 até 2
texto[2:]     # "thon"     → do índice 2 até o fim
texto[:4]     # "Pyth"     → do início até o índice 3
texto[::-1]   # "nohtyP"   → string invertida!   


