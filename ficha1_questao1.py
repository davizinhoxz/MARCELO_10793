from random import randint

lista = []
Npares = 0
Nimpares = 0
media = 0
maiorMedia = 0
listaDaMaiorMedia = []

for i in range(30):
    numero_aleatorio = randint(1, 100) 
    lista.append(numero_aleatorio)
    media = (sum(lista)/len(lista))
    
    if lista[i] % 2 == 0:
        Npares += 1
    else: 
        Nimpares += 1


    if lista[i] > media:
        maiorMedia += 1
        listaDaMaiorMedia.append(numero_aleatorio)


print(lista)
print(f"Existem {Npares} Números pares")
print(f"Existem {Nimpares} Números ímpares")
print(f"O Maior número da lista é {max(lista)}")
print(f"O Menor número da lista é {min(lista)}")
print(f"A média dos números da lista é {round(media)}")
print(f"{maiorMedia} números são maiores que a média")
print(listaDaMaiorMedia)