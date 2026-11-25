# Crie uma função:
# maior_numero(a, b)
# Ela deve receber dois números e retornar o maior.
# Não use max(). Faça a comparação usando if/else.

def maior_numero(a, b):
    if a > b:
        return a
    else:
        return b

print(maior_numero(10, 5))
print(maior_numero(24, 50))
print(maior_numero(12, 89))
print(maior_numero(24, 5))