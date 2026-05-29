salario_bruto = float(input("Digite seu Salário: "))
reajuste1 = salario_bruto * 0.20
reajuste2 = salario_bruto * 0.15
reajuste3 = salario_bruto * 0.10
reajuste4 = salario_bruto * 0.05

if salario_bruto <= 280:
   print(f"O seu salario era {salario_bruto}, com reajuste de 20% seu salario vai para {reajuste1} ")
elif salario_bruto <= 700:
   print(f"O seu salario era {salario_bruto}, com reajuste de 20% seu salario vai para {reajuste2}") 
elif salario_bruto <= 1500:
   print(f"O seu salario era {salario_bruto}, com reajuste de 20% seu salario vai para {reajuste3}")  
 