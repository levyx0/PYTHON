#Fatiamento (ou slicing) é uma técnica para extrair parte de uma string usando índices. É muito útil para manipular textos.

palavra = "Programação"

# Pegar do índice 0 ao 3 (sem incluir o 3)
print(palavra[0:3])      # Saída: Pro

# Se omitir o início, começa do 0
print(palavra[:3])       # Saída: Pro

# Se omitir o fim, vai até o final
print(palavra[4:])      # Saída: mação

# De um ponto até outro
print(palavra[3:7])     # Saída: ram

# Sem especificar inicio e fim (copia toda string)
print(palavra[:])       # Saída: Programação