# Crie uma função eh_par(numero) que retorne:
# True
# se o número for par e:
# False
# se for ímpar.
# Teste com vários números.

def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

print(eh_par(10))
print(eh_par(3))
print(eh_par(24))
print(eh_par(7))
print(eh_par(30))