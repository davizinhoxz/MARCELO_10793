import random

print("-----BATALHA-----")

jogador = {
    "vida": 300,
    "ataque": 20,
    "pocoes": 2,
    "pontos": 0,
    "derrotados": 0
}


tipoDeInimigos = [
    {"nome": "Goblin", "vida": 40, "ataque": 8, "pontos": 100},
    {"nome": "Orc", "vida": 55, "ataque": 11, "pontos": 200},
    {"nome": "Troll", "vida": 70, "ataque": 14, "pontos": 300},
    {"nome": "Beast", "vida": 85, "ataque": 17, "pontos": 400},
    {"nome": "Dragão", "vida": 100, "ataque": 20, "pontos": 500}
]


selecao = random.randint(3, 5)
#pra nao repetir
inimigos = random.sample(tipoDeInimigos, selecao)


jogo = True
resultado = ""

while jogo:
    print("========== BATALHA ==========")
    print("1 — Atacar inimigo")
    print("2 — Consultar estado do jogador")
    print("3 — Listar inimigos vivos")
    print("4 — Usar poção de cura")
    print("5 — Fugir / terminar jogo")

    opcao = int(input("\nEscolha a opção: "))

    match opcao:
        case 1:
            vivos = []
            for inimigo in inimigos:
                if inimigo["vida"] > 0:
                    vivos.append(inimigo)
            if len(vivos) == 0:
                print("Não existem inimigos vivos")
            else:
                print("\nInimigos vivos:")
                for i in range(len(vivos)):
                    print(i + 1, "-", vivos[i]["nome"], "- Vida:", vivos[i]["vida"])
                escolha = input("Escolha o inimigo: ")
                ...

        case 2:
            print("\n-----ESTADO-DO-JOGADOR-----")
            print("Vida:", jogador["vida"])
            print("Pontuação:", jogador["pontos"])
            print("Inimigos Derrotados:", jogador["derrotados"])
            print("Inimigos Vivos:", len(inimigos) - jogador["derrotados"])
            print("Poções:", jogador["pocoes"])

        case 3:
            print("\n-----INIMIGOS-VIVOS-----")
            for inimigo in inimigos:
                if inimigo["vida"] > 0:
                    print("Nome:", inimigo["nome"])
                    print("Vida:", inimigo["vida"])
                    print("Ataque:", inimigo["ataque"])

        case 4:
            if jogador["pocoes"] == 0:
                print("Voce não tem mais poções")
                
            elif jogador["vida"] >= 100:
                print("Não pode usar poção: já tem 100 ou mais pontos de vida")
                
            else:
                jogador["vida"] += 25
                jogador["pocoes"] -= 1
                if jogador["vida"] > 100:
                    jogador["vida"] = 100
                print("Voce usou uma poção e a sua Vida atual é: ", jogador["vida"])
                print("Agora voce tem: ", jogador["pocoes"], "poções.")

        case 5:
            print("A partida terminou porque voce fugiu")
            resultado = "FUGA"
            jogo = False

    if jogador["vida"] <= 0:
        print("\nVoce perdeu")
        resultado = "DERROTA"
        jogo = False
        
    elif jogador["derrotados"] == len(inimigos):
        print("\nPARABENS! GANHOU DE TODO MUNDO")
        resultado = "VITÓRIA"
        jogo = False

print("\n-------RESULTADO-FINAL-------")
print("Resultado:", resultado)
print("Pontuação:", jogador["pontos"])
print("Inimigos derrotados:", jogador["derrotados"])
