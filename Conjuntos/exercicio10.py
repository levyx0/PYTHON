#Participantes de eventos

# evento_a = {"Ana", "Bruno", "Carlos", "Diana"}
# evento_b = {"Bruno", "Diana", "Eduardo"}
# evento_c = {"Ana", "Diana", "Eduardo", "Felipe"}

# Responda usando código:
# 1. Quem participou dos três eventos?
# 2. Quem participou de pelo menos um evento?
# 3. Quem participou do evento A, mas não do evento B?
# 4. Quantas pessoas diferentes participaram no total?

evento_a = {"Ana", "Bruno", "Carlos", "Diana"}
evento_b = {"Bruno", "Diana", "Eduardo"}
evento_c = {"Ana", "Diana", "Eduardo", "Felipe"}

#Participaram dos 3 Eventos
print(evento_a & evento_b & evento_c)
#Participaram de pelo menos um evento
print(evento_a - evento_b - evento_c)
#Particou do Evento A, mas não do Evento B
print(evento_a - evento_b)
#Quantas pessoas diferentes participaram no total
print(evento_a | evento_b | evento_c)