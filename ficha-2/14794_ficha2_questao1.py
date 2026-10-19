listaTarefas = []

print("GERIR AS TAREFAS")

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

num_tarefa = [1,11]

num_tarefa = input("Número da tarefa desejada: ")


match num_tarefa:
    case 1:
        listaTarefas.append(input("Qual a próxima tarefa? "))
    case 2:
        listaTarefas.extend(input("Quais as próximas tarefas? "))
    case 3:
        listaTarefas.insert(int(input("Diga a posição da tarefa que deseja inserir: ")), input("Agora qual tarefa quer inserir: "))
    case 4:
        listaTarefas.remove(input("Remova a tarefa desejada pelo nome que escreveu: "))
    case 5:
        listaTarefas.pop()
    case 6:
        listaTarefas.clear()
    case 7:
        listaTarefas.count(input("Digite a tarefa que quer ver o nº de vezes que ela aparece: "))
    case 8:
        listaTarefas.index(input("Digite a tarefa que quer ver a posição: "))
    case 9:
        listaTarefas.sort()
    case 10:
        listaTarefas.reverse()
    case 11:
        listaTarefas