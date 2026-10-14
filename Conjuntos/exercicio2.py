#Você tem duas listas de produtos vendidos em dias diferentes:

# dia_1 = ["perfume", "shampoo", "creme", "perfume"]
# dia_2 = ["shampoo", "sabonete", "creme", "sabonete"]

# Crie uma função chamada analisar_vendas(dia_1, dia_2) que:
# 1. Transforme as duas listas em conjuntos.
# 2. Mostre todos os produtos diferentes vendidos nos dois dias, sem duplicatas.
# 3. Mostre quais produtos foram vendidos nos dois dias.
# 4. Retorne a quantidade de produtos diferentes vendidos no total.
# Dica: você já conhece todas as ferramentas necessárias: set(), |, &, len() e return.
# Tente escrever o código e me envie. Vou corrigir seu raciocínio do mesmo jeito, analisando o que você fez antes de sugerir alterações.

dia_1 = ["perfume", "shampoo", "creme", "perfume"]
dia_2 = ["shampoo", "sabonete", "creme", "sabonete"]

def analisar_vendas(dia_1, dia_2):
    conj1 = set(dia_1) #{"perfume", "shampoo", "creme"}
    conj2 = set(dia_2) #{"shampoo", "sabonete", "creme"}

    todos = conj1 | conj2
    nos_dois = conj1 & conj2

    print("Todos os produtos vendidos: ", todos)
    print("Vendidos nos dois dias: ", nos_dois)

    return len(todos)

quantidade = analisar_vendas(dia_1, dia_2)
print("Quantidade de produtos diferentes: ", quantidade)
