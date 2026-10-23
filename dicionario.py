aluno = {   "nome": "Carlos",
            "idade": 17,
            "cidade": "Famalicao",
            "disciplinas": ["Matemática", "Programação", "Inglês"],
            "notas": { "matematica": [17.5,12], "programacao": [20,13], "ingles": [12.25,7.75]}
            }

print(aluno["nome"])
# Altero valor de uma chave
aluno["idade"] = 18
# Inserir uma nova chave
aluno["estado_civil"] = "Solteiro"
print(aluno)
# Imprimir as caracteristicas do aluno
for chave in aluno.keys():
    print(f"{chave}", end=" ")
# Imprimir somnte os valores
print()
for valor in aluno.values():
    print(f"{valor}", end=" ")
# Imprimir a chave e o valor
print()
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

aluno["disciplinas"].append("Português")
for disciplina in aluno["disciplinas"]:
    print(disciplina)

print(aluno["notas"]["programacao"][1])

# Média de todas as notas
soma = 0
n_notas = 0
for notas_disciplinaa in aluno["notas"].values():
    soma += sum(notas_disciplinaa)
    n_notas += len(notas_disciplinaa)

    # pares = [num for num in lista if num % 2 == 0]