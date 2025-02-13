jogada1 = 0
jogada2 = 0

def defina_jogo(jogada):
    if jogada != 1 | 2 | 3 | 4:
        return False
    return True

def escolha_jogador(jogador):
    while (escolha_jogador != 3):
        if jogador == 1:
            jogada = jogada1
        else:
            if jogador == 2:
                jogada = jogada2
            else:
                break


def result_jogo(resultado):
    if jogada1 == 1 & jogada2 == 2:
        print("\n\nJogador 2 venceu!")
    else:
        if jogada1 == 2 & jogada2 == 1:
            print("\n\nJogador 1 venceu!")
        else:
            if jogada1 == 2 & jogada2 == 3:
                print("\n\nJogador 2 venceu!")
            else:
                if jogada1 == 3 & jogada2 == 2:
                    print("\n\nJogador 1 venceu!")
                else:
                    if jogada1 == 1 & jogada2 == 3:
                        print("\n\nJogador 1 venceu!")
                    else:
                        if jogada1 == 3 & jogada2 == 1:
                            print("\n\nJogador 2 venceu!")

escolha_jogador = int(input("Qual jogador irá fazer a jogada?\n\n1) Jogador 1\n2) Jogador 2\n3) Sair\n\nInsira: "))
jogada = int(input("Faça sua jogada:\n1) Pedra\n2) Papel\n3) Tesoura\n\nInsira: "))

if jogada == True:
    if jogada == 1:
        print("Pedra")
    else:
        if jogada == 2:
            print("Papel")
        else:
            if jogada == 3:
                print("Tesoura")
else:
    print("Opção inválida!")
