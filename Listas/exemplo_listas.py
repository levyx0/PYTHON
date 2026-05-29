# Sistema simples de lista de tarefas

tarefas =  []

while True:
    print("\n1 - Adcionar tarefa")
    print("2 - Remover Tarefas")
    print("3 - Ver tarefas")
    print("0 - Sair")

    opcao = input("Esolha uma Opção: ")

    if opcao == "1":
       tarefa = input("Digite a Tarefa: ")
       tarefas.append(tarefa)
       print("Tarefa Adcionada!")

    elif opcao == "2":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada!")
        else:
            for i, tarefa in enumerate(tarefas):
                print(f"{i} - {tarefa}") 
            indice = int(input("Qual a indice remover?: "))
            tarefas.pop(indice)
            print("Tarefa Removida!")

    elif opcao == "3":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada!")
        else: 
            for i, tarefa in enumerate(tarefas):  
                print(f"{i}  - {tarefa}")
                

    elif opcao == "0":
        print("Até Logo!")
        break
        
  