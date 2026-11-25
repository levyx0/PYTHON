# futebol = {"Carlos", "Ana", "Pedro", "João"}
# volei = {"Ana", "Mariana", "João", "Lucas"}

# 1. Descubra quais pessoas praticam os dois esportes.
# 2. Conte quantas são.
# 3. Verifique se "Pedro" pratica os dois esportes.
# Conceitos: interseção (&) e in.

futebol = {"Carlos", "Ana", "Marcos", "Pedro"}
volei = {"Giovanna", "Mariana","Marcos", "Ana"}
#praticam esporte em comum.
print(futebol & volei)
#quantidade de pessoas no mesmo esporte.
print(len(futebol & volei))
#verificando se "pedro" pratica os dois sportes

if "Pedro" in futebol and "Pedro" in volei:
    print("Participa nos dois esportes")
else:
    print("Não participa dos dois esportes")    