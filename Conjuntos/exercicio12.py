# Controle de clientes
# Uma loja possui duas listas de clientes:
# clientes_mes_passado = ["Ana", "João", "Pedro", "Ana", "Lucas"]
# clientes_mes_atual = ["João", "Maria", "Lucas", "Carlos"]

# Crie uma função analisar_clientes() que receba as duas listas e retorne um dicionário contendo:
# - clientes_unicos: todos os clientes sem duplicatas.
# - clientes_recorrentes: clientes presentes nos dois meses.
# - novos_clientes: clientes do mês atual que não aparecem no mês passado.
# - total_unicos: quantidade de clientes diferentes.
# Conceitos: conjuntos, funções, dicionários, listas e len().


def analisar_clientes(cliente_mes_passado, cliente_mes_atual):
    passado = set(cliente_mes_passado)
    atual = set(cliente_mes_atual)

    resultado = {
        "Clientes_unicos": passado | atual,
        "Clientes_recorrentes": passado & atual,
        "Novos_Clientes": atual - passado,
        "Total_unicos": len(passado | atual)    
      }

    return resultado

clientes_mes_passado = ["Ana", "João", "Pedro", "Ana", "Lucas"]
clientes_mes_atual = ["João", "Maria", "Lucas", "Carlos"]

analise = analisar_clientes(clientes_mes_passado, clientes_mes_atual)
print(analise)