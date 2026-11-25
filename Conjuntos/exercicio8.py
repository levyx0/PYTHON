# comprados = {"perfume", "creme", "sabonete", "shampoo"}
# estoque = {"perfume", "creme", "shampoo"}

# 1. Descubra quais produtos foram comprados, mas não estão no estoque.
# 2. Descubra quais produtos estão no estoque, mas não aparecem na lista de compras.
# Conceito: diferença (-).

comprados = {"perfume", "creme", "sabonete", "shampoo"}
estoque = {"perfume", "creme", "shampoo"}

print(comprados - estoque)

print(estoque - comprados)