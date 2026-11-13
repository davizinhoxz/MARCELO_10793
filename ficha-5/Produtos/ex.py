# gerar números aleatórios
import random

print("========== BATALHA ==========")

jogador = {
    "vida": 300,       
    "ataque": 20,    
    "pocoes": 2,        
    "pontos": 0,       
    "derrotados": 0     
}

tipos_inimigos = [
    {"nome": "Goblin", "vida": 40, "ataque": 8, "pontos": 100},
    {"nome": "Orc", "vida": 55, "ataque": 11, "pontos": 200},
    {"nome": "Troll", "vida": 70, "ataque": 14, "pontos": 300},
    {"nome": "Beast", "vida": 85, "ataque": 17, "pontos": 400},
    {"nome": "Dragão", "vida": 100, "ataque": 20, "pontos": 500}
]

quantidade = random.randint(3, 5)

# random.sample escolhe sem repetir os inimigos
inimigos = random.sample(tipos_inimigos, quantidade)


jogo = True

while jogo:

    print("\n========== BATALHA ==========")
    print("1 - Atacar inimigo")
    print("2 - Consultar estado do jogador")
    print("3 - Listar inimigos vivos")
    print("4 - Usar poção de cura")
    print("5 - Fugir / terminar jogo")

    opcao = input("Escolha uma opção: ")


    if opcao == "1":

        vivos = []


        for inimigo in inimigos:


            if inimigo["vida"] > 0:


                vivos.append(inimigo)



        if len(vivos) == 0:

            print("Não existem inimigos vivos!")

        else:

            print("\nInimigos vivos:")


            for i in range(len(vivos)):


                print(i + 1, "-", vivos[i]["nome"],
                      "- Vida:", vivos[i]["vida"])


            escolha = input("Escolha o inimigo: ")


            if escolha.isdigit():

                numero = int(escolha)


                if numero >= 1 and numero <= len(vivos):

                    inimigo = vivos[numero - 1]


                    dano = random.randint(10, 20)



                    inimigo["vida"] -= dano



                    if inimigo["vida"] < 0:

                        inimigo["vida"] = 0


                    print("Causaste", dano, "de dano!")
                    print("Vida do inimigo:", inimigo["vida"])


                    if inimigo["vida"] == 0:

                        print("Derrotaste o", inimigo["nome"])


                        jogador["pontos"] += inimigo["pontos"]



                        jogador["derrotados"] += 1

                    else:

                        dano_inimigo = random.randint(
                            5, inimigo["ataque"]
                        )


                        jogador["vida"] -= dano_inimigo


                        if jogador["vida"] < 0:

                            jogador["vida"] = 0


                        print("O inimigo contra-atacou!")
                        print("Recebeste", dano_inimigo, "de dano!")
                        print("Vida atual:", jogador["vida"])

                else:

                    print("Número de inimigo inválido!")

            else:

                print("Escolha inválida!")



    elif opcao == "2":

        print("\n-----ESTADO-DO-JOGADOR-----")

        print("Vida:", jogador["vida"])

        print("Pontos:", jogador["pontos"])

        print("Inimigos derrotados:", jogador["derrotados"])


        print("Inimigos vivos:",
              len(inimigos) - jogador["derrotados"])

        print("Poções:", jogador["pocoes"])



    elif opcao == "3":

        print("\n-----INIMIGOS-VIVOS-----")


        contador = 0


        for inimigo in inimigos:

            if inimigo["vida"] > 0:

                print("Nome:", inimigo["nome"])
                print("Vida:", inimigo["vida"])
                print("Ataque:", inimigo["ataque"])
                print("-------------------")


                # Somamos 1 ao contador
                contador += 1


        if contador == 0:

            print("Não existem inimigos vivos!")


    elif opcao == "4":


        if jogador["pocoes"] == 0:

            print("Não tens poções disponíveis!")



        elif jogador["vida"] >= 300:

            print("Já tens a vida máxima!")


        else:

            jogador["vida"] += 25

            jogador["pocoes"] -= 1


            if jogador["vida"] > 300:

                jogador["vida"] = 300


            print("Usaste uma poção!")
            print("Vida atual:", jogador["vida"])
            print("Poções restantes:", jogador["pocoes"])



    elif opcao == "5":

        print("Terminaste a partida por FUGA!")


        jogo = False



    else:

        print("Opção inválida!")



    if jogador["vida"] == 0:

        print("\nFoste derrotado!")

        jogo = False



    elif jogador["derrotados"] == len(inimigos):

        print("\nVITÓRIA! Derrotaste todos os inimigos!")

        # Terminamos o jogo
        jogo = False


# ============================================
# RESULTADO FINAL
# ============================================

# Estas instruções estão fora do while
# Só são executadas quando o jogo terminar

print("\n===== RESULTADO FINAL =====")

# Mostramos a pontuação conseguida
print("Pontuação:", jogador["pontos"])

# Mostramos o total de inimigos derrotados
print("Inimigos derrotados:", jogador["derrotados"])
