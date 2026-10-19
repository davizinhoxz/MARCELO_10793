from random import randint

notas = []
inside = 0
out = 0
notaBoa = 0
media = 0

for _ in range(15):
    numero_aleatorio = randint(0, 20) 
    notas.append(numero_aleatorio)
    media = (sum(notas)/len(notas))


    if numero_aleatorio >= 10:
        inside += 1
        if numero_aleatorio >= 16:
            notaBoa += 1
    else:
        out += 1

print(f"{inside} foram aprovados")
print(f"{out} foram reprovados")
print(f"A Maior nota da lista é {max(notas)}")
print(f"A Maior nota da lista é {min(notas)}")
print(f"A média das notas da lista é {media}")
print(f"A porcentagem de aprovação da turma é {round(inside/len(notas)*100)}")