jogadores = ["J1", "J2", "J3"]

# INSERIR UM JOGADOR
jogadores.append("J4") # ["J1", "J2", "J3", "J4"]

# INSERIR VARIOS
jogadores.extend("J5", "J6") # ["J1", "J2", "J3", "J4", "J5", "J6"]
nj = ["J7", "J8"] # ["J1", "J2", "J3", "J4", "J5", "J6", "J7", "J8"]
jogadores.extend(nj)

# INSERIR UM EM UMA POSIÇÃO ESPECIFICA
jogadores.insert(2, "J9") #["J1", "J2", "J9", "J3", "J4", "J5", "J6", "J7", "J8"]

# REMOVER O ÚLTIMO JOGADOR
jogadores.pop() #["J1", "J2", "J9", "J3", "J4", "J5", "J6", "J7"]

# REMOVER UM EM UMA POSIÇÃO ESPECIFICA
jogadores.pop(4) #["J1", "J2", "J9", "J4", "J5", "J6", "J7"]

# REMOVER JOGADOR PELO NOME
jogadores.remove("J6") #["J1", "J2", "J9", "J4", "J5", "J7"]

# SABER O N DE JOGADORES
y = len(jogadores) # = 6

# copiar uma lista
lista1 = [1, 2, 3]
lista2 = lista1
print(lista1,lista2)
lista1.append(5)
...