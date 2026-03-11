# GERENCIADOR DE TAREFAS 2

tarefas = []

def adicionar_tarefa():
    descricao = input("Digite a nova tarefa: ")
    
    nova_tarefa = {"nome": descricao, 
    "status": False}
    
    tarefas.append(nova_tarefa)
    print("\n=========== Tarefa adicionada! ===========")
    print("->", descricao)

def ver_tarefas():
    
    print("\n=========== Sua lista de tarefas ===========")

    if len(tarefas) == 0:
        print("=========== Nenhuma tarefa cadastrada! ===========")
        return
    
    for i, tarefa in enumerate(tarefas):
        
        if tarefa['status']:
            status = '✅'
        else:
            status = '❌'
        print(f"{i+1}. {tarefa['nome']} [{status}]")

def concluir_tarefa():

    ver_tarefas()
    try:
        concluir = int (input ("Digite qual tarefa deseja concluir: "))
    
        tarefas[concluir - 1] ['status'] = True
        print("=========== Tarefa concluida! ===========")

    except (ValueError, IndexError):
        print("Digite um número válido!")

def remover_tarefa():
 
 ver_tarefas()

 try:
    numero = int(input("Qual tarefa deseja remover?: "))
 
    tarefa_removida = tarefas.pop(numero - 1)
    print(f"Tarefa '{tarefa_removida['nome']}' removida.")
 
 except (ValueError, IndexError):
    print("Digite um número válido!")
 
 
while True:
    print("\n####################")
    print("\n[1] Adicionar tarefa")
    print("\n[2] Ver tarefa")
    print("\n[3] Concluir tarefa")
    print("\n[4] Remover tarefa")
    print("\n[5] Sair")
    print("\n####################")

    try:
        opcao = int(input("Escolha uma opção!: "))

        if opcao == 1:
             adicionar_tarefa() #DEFINIR "REMOVER_TAREFA" COMO FUNÇÃO
        elif opcao == 2:
             ver_tarefas() #DEFINIR "REMOVER_TAREFA" COMO FUNÇÃO
        elif opcao == 3:
            concluir_tarefa() #DEFINIR "REMOVER_TAREFA" COMO FUNÇÃO
        elif opcao == 4:
            remover_tarefa() #DEFINIR "REMOVER_TAREFA" COMO FUNÇÃO
        elif opcao == 5:
            print("=========== SAINDO DO PROGRAMA.... ===========")
            break
    except ValueError:
         print("Digite um número válido! (Não digite letra!)")
