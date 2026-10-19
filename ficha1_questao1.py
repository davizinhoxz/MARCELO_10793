from random import randint

lista = []
pares = 0
impares = 0
media = 0
maiorQueMed = 0

for n in range(30):
    numero_aleatorio = randint(1, 100)

    media = (sum(lista)/len(lista))