from random import randint
import os

#x = randint

resposta = 'S'

while resposta == 'S':
    os.system("clear")
    #declarar ....
    tentativas = 0
    pontuacao = 0
    pontuacoes = [100, 80, 60, 40, 30, 20, 10]
    numGerado = randint(1,100)
    print(numGerado)

    #Ciclo de Tentativas
    while tentativas < 7:
        meuNum = int(input("Tente o valor: "))

        while meuNum < 1 or meuNum > 100:
            print("Impossível! O número deve estar entre 1 e 100!")
            meuNum = int(input("Tente denovo: "))
        
        os.system("clear")
        tentativas = tentativas + 1

        if meuNum == numGerado:
            print(f"Boa, acertou o número em {tentativas} tentativas.")

            pontuacao = pontuacoes[tentativas-1]

            print(f"E fez {pontuacao} pontos!49")

            # if tentativas == 1:
            #     print("E fez 100 pontos!")
            # elif tentativas == 2:
            #     print("E fez 80 pontos!")
            # elif tentativas == 3:
            #     print("E fez 60 pontos!")
            # elif tentativas == 4:
            #     print("E fez 40 pontos!")
            # elif tentativas == 5:
            #     print("E fez 30 pontos!")
            # elif tentativas == 6:
            #     print("E fez 20 pontos!")
            # elif tentativas == 7:
            #     print("E fez 10 pontos!")

            break

        if meuNum < numGerado:
            print("O número que você quer descobrir é maior!")
        else:
            print("O número que você quer descobrir é menor!")

    if tentativas >= 7 and meuNum != numGerado:
        print(f"Sinto muito! O número gerado foi {numGerado}")

    resposta = (input("Deseja jogar denovo? (S/N)")).upper()
