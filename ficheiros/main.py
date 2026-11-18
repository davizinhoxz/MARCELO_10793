import json


f = open("ficheiros/dados.txt","r")
lista = f.readlines()

for linha in lista:
    print(linha.strip())
    
    
with open("ficheiros/nomes.txt","w") as file:
    file.write("Davi\n")
    file.write("Pastel\n")
    
    
    
with open("ficheiros/nomes.txt","a") as file:
    file.write("Dinis\n")
    file.write("AC Milan\n")
#conteudo = f.read()

with open("nomes.json","r") as f:
    dados = json.load(f)
    
print(dados)
nome = {"nome": "Davi", "idade": 27}
dados.append(nome)


with open("nomes.json", "w") as f:
    json.dump(dados,f,indent=4)
    


