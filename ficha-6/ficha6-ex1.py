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

        # Criamos uma lista vazia para guardar os inimigos vivos
        vivos = []

        # Percorremos todos os inimigos existentes
        for inimigo in inimigos:

            # Verificamos se o inimigo ainda tem vida
            if inimigo["vida"] > 0:

                # Se tiver vida, adicionamos à lista de vivos
                vivos.append(inimigo)


        # Se a lista estiver vazia, não existem inimigos vivos
        if len(vivos) == 0:

            print("Não existem inimigos vivos!")

        else:

            # Mostramos os inimigos que ainda estão vivos
            print("\nInimigos vivos:")

            # O range cria números de 0 até ao tamanho da lista - 1
            for i in range(len(vivos)):

                # Mostramos o número, nome e vida do inimigo
                # Usamos i + 1 porque queremos começar a contar em 1
                print(i + 1, "-", vivos[i]["nome"],
                      "- Vida:", vivos[i]["vida"])


            # Pedimos ao jogador para escolher um inimigo
            escolha = input("Escolha o inimigo: ")


            # isdigit verifica se o utilizador escreveu apenas números
            # Isto evita erros se escrever letras
            if escolha.isdigit():

                # Convertemos o texto introduzido para inteiro
                numero = int(escolha)


                # Verificamos se o número está dentro dos disponíveis
                if numero >= 1 and numero <= len(vivos):

                    # Guardamos o inimigo escolhido numa variável
                    # Usamos numero - 1 porque as listas começam em 0
                    inimigo = vivos[numero - 1]


                    # Geramos um dano aleatório entre 10 e 20
                    dano = random.randint(10, 20)


                    # Retiramos o dano à vida do inimigo
                    # -= significa subtrair ao valor atual
                    inimigo["vida"] -= dano


                    # A vida do inimigo nunca pode ser negativa
                    if inimigo["vida"] < 0:

                        inimigo["vida"] = 0


                    # Mostramos o resultado do ataque
                    print("Causaste", dano, "de dano!")
                    print("Vida do inimigo:", inimigo["vida"])


                    # Verificamos se o inimigo morreu
                    if inimigo["vida"] == 0:

                        print("Derrotaste o", inimigo["nome"])


                        # Adicionamos os pontos do inimigo
                        # à pontuação total do jogador
                        jogador["pontos"] += inimigo["pontos"]


                        # Aumentamos o número de inimigos derrotados
                        jogador["derrotados"] += 1

                    else:

                        # Se o inimigo continuar vivo, contra-ataca
                        # O dano é aleatório entre 5 e o ataque do inimigo
                        dano_inimigo = random.randint(
                            5, inimigo["ataque"]
                        )


                        # Retiramos o dano à vida do jogador
                        jogador["vida"] -= dano_inimigo


                        # Impedimos que a vida fique negativa
                        if jogador["vida"] < 0:

                            jogador["vida"] = 0


                        # Mostramos o resultado do contra-ataque
                        print("O inimigo contra-atacou!")
                        print("Recebeste", dano_inimigo, "de dano!")
                        print("Vida atual:", jogador["vida"])

                else:

                    # O jogador escolheu um número fora da lista
                    print("Número de inimigo inválido!")

            else:

                # O jogador escreveu algo que não é um número
                print("Escolha inválida!")


    # ============================================
    # OPÇÃO 2 - CONSULTAR ESTADO DO JOGADOR
    # ============================================

    elif opcao == "2":

        print("\n===== ESTADO DO JOGADOR =====")

        # Mostramos a vida atual
        print("Vida:", jogador["vida"])

        # Mostramos os pontos acumulados
        print("Pontos:", jogador["pontos"])

        # Mostramos quantos inimigos já foram derrotados
        print("Inimigos derrotados:", jogador["derrotados"])

        # Calculamos quantos inimigos continuam vivos
        # Total de inimigos menos inimigos derrotados
        print("Inimigos vivos:",
              len(inimigos) - jogador["derrotados"])

        # Mostramos quantas poções ainda estão disponíveis
        print("Poções:", jogador["pocoes"])


    # ============================================
    # OPÇÃO 3 - LISTAR INIMIGOS VIVOS
    # ============================================

    elif opcao == "3":

        print("\n===== INIMIGOS VIVOS =====")


        # Criamos um contador para contar os inimigos vivos
        contador = 0


        # Percorremos todos os inimigos
        for inimigo in inimigos:

            # Verificamos se o inimigo ainda tem vida
            if inimigo["vida"] > 0:

                # Mostramos as informações do inimigo
                print("Nome:", inimigo["nome"])
                print("Vida:", inimigo["vida"])
                print("Ataque:", inimigo["ataque"])
                print("-------------------")


                # Somamos 1 ao contador
                contador += 1


        # Se o contador for 0, não existem inimigos vivos
        if contador == 0:

            print("Não existem inimigos vivos!")


    # ============================================
    # OPÇÃO 4 - USAR POÇÃO DE CURA
    # ============================================

    elif opcao == "4":


        # Primeiro verificamos se o jogador tem poções
        if jogador["pocoes"] == 0:

            print("Não tens poções disponíveis!")


        # Verificamos se a vida já está no máximo
        elif jogador["vida"] >= 300:

            print("Já tens a vida máxima!")


        else:

            # Adicionamos 25 pontos à vida do jogador
            jogador["vida"] += 25


            # Retiramos uma poção do inventário
            jogador["pocoes"] -= 1


            # Verificamos se a vida ultrapassou o limite
            if jogador["vida"] > 300:

                # Se ultrapassar, colocamos a vida em 300
                jogador["vida"] = 300


            # Mostramos o resultado
            print("Usaste uma poção!")
            print("Vida atual:", jogador["vida"])
            print("Poções restantes:", jogador["pocoes"])


    # ============================================
    # OPÇÃO 5 - FUGIR DO JOGO
    # ============================================

    elif opcao == "5":

        # Mostramos que o jogador fugiu
        # A fuga não conta como vitória
        print("Terminaste a partida por FUGA!")


        # Alteramos a variável jogo para False
        # Isto faz com que o while termine
        jogo = False


    # ============================================
    # OPÇÃO INVÁLIDA
    # ============================================

    else:

        # Se escolher algo diferente de 1, 2, 3, 4 ou 5
        # mostramos uma mensagem de erro
        print("Opção inválida!")


    # ============================================
    # VERIFICAR SE O JOGO TERMINOU
    # ============================================


    # Verificamos se a vida do jogador chegou a zero
    if jogador["vida"] == 0:

        print("\nFoste derrotado!")

        # Terminamos o jogo
        jogo = False


    # Verificamos se todos os inimigos foram derrotados
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
