# Exercício 3 — Contador de vogais
# Peça uma frase ao usuário e conte quantas vogais ela tem, exibindo o resultado assim:
# Frase: "Python é incrível"
# a: 1 | e: 2 | i: 2 | o: 1 | u: 0
# Total de vogais: 6

# 💡 Dica: lower(), count()

print("CONTADOR DE VOGAIS")

frase = input("Escreva uma frase: ").lower()

#contando Vogais
a = frase.count("a")
e = frase.count("e")
i = frase.count("i") 
o = frase.count("o") 
u = frase.count("u") 

#Soma total
total = a + e + i + o + u

#Exibindo resultado
print(f"a: {a} | e {e} | i {i} | o {o} | u {u}")
print(f"Total de Vogais: {total}")
