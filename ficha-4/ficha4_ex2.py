txt = "Davi Nascimento"
contagem = {}


for nLetra in txt:
    nLetra = nLetra.lower()

    if nLetra.isspace() == False:
        if nLetra in contagem.keys():
            contagem[nLetra] += 1

        else:
            contagem[nLetra] = 1

print(contagem)