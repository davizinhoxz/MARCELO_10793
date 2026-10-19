from random import randint


notas = []
aprovados = 0
reprovados = 0
notaAlta = 0
media = 0


for _ in range(15):
    numero_aleatorio = randint(0, 20) 
    notas.append(numero_aleatorio)
    media = (sum(notas)/len(notas))


    if numero_aleatorio >= 10:
        aprovados += 1
        if numero_aleatorio >= 16:
            notaAlta += 1
    else:
        reprovados += 1


print(f"{aprovados} foram aprovados")
print(f"{reprovados} foram reprovados")
print(f"A Maior nota da lista é {max(notas)}")
print(f"A Maior nota da lista é {min(notas)}")
print(f"A média das notas da lista é {media}")
print(f"A porcentagem de aprovação da turma é {round(aprovados/len(notas)*100)}")