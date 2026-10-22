listaTarefas = []

while True:

    print("\nGERIR AS TAREFAS")

    print("1. Adicionar Tarefa.")
    print("2. Adicionar Múltiplas Tarefas.")
    print("3. Inserir Tarefa em uma Posição Específica.")
    print("4. Remover Tarefa pelo Nome.")
    print("5. Remover A Última Tarefa.")
    print("6. Remover todas as Tarefas.")
    print("7. Contar Ocorrências de Tarefa.")
    print("8. Encontrar Índice de Tarefa.")
    print("9. Ordenar Tarefas: Organizar as tarefas em ordem alfabética.")
    print("10. Inverter Ordem das Tarefas: Reverter a ordem atual das tarefas.")
    print("11. Copiar Lista de Tarefas: Criar uma cópia independente da lista de tarefas.")
    print("0. Acabar.")

    num_tarefa = int(input("\nNúmero da tarefa desejada: "))

    match num_tarefa:
        case 1:
            tarefa = input("Qual a próxima tarefa? ")
            listaTarefas.append(tarefa)

        case 2:
            tarefas = input("Quais as próximas tarefas, separadas por vírgula: ")
            tarefas = tarefas.split(",")
            listaTarefas.extend(tarefas)

        case 3:
            posicao = int(input("Diga a posição da tarefa que deseja inserir: "))
            tarefa = input("Agora qual tarefa quer inserir: ")
            listaTarefas.insert(posicao, tarefa)

        case 4:
            tarefa = input("Remova a tarefa desejada pelo nome que escreveu: ")
            listaTarefas.remove(tarefa)

        case 5:
            listaTarefas.pop()

        case 6:
            listaTarefas.clear()

        case 7:
            tarefa = input("Digite a tarefa que quer ver o nº de vezes que ela aparece: ")
            contador = listaTarefas.count(tarefa)
            print(f"A tarefa aparece {contador} vez(es).")

        case 8:
            tarefa = input("Digite a tarefa que quer ver a posição: ")
            indice = listaTarefas.index(tarefa)
            print(f"Posição: {indice}.")

        case 9:
            listaTarefas.sort()

        case 10:
            listaTarefas.reverse()

        case 11:
            copia_da_lista = listaTarefas.copy()
            print(copia_da_lista)

        case 0:
            break

    print("\nLista atual:", listaTarefas)