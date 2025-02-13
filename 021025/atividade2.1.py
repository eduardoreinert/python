def jogar():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    
    while True:
        while True:
            try:
                jogador1 = int(input("Jogador 1 - Escolha: 0 (Pedra), 1 (Papel) ou 2 (Tesoura): "))
                if jogador1 in [0, 1, 2]:  
                    break
                else:
                    print("Opção inválida! Digite 0, 1 ou 2.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

        while True:
            try:
                jogador2 = int(input("Jogador 2 - Escolha: 0 (Pedra), 1 (Papel) ou 2 (Tesoura): "))
                if jogador2 in [0, 1, 2]:  
                    break
                else:
                    print("Opção inválida! Digite 0, 1 ou 2.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

        print(f"\nJogador 1 escolheu: {opcoes[jogador1]}")
        print(f"Jogador 2 escolheu: {opcoes[jogador2]}")

        if jogador1 == jogador2:
            print("Empate!")
        elif (jogador1 == 0 and jogador2 == 2) or (jogador1 == 1 and jogador2 == 0) or (jogador1 == 2 and jogador2 == 1):
            print("Jogador 1 venceu!")
        else:
            print("Jogador 2 venceu!")

        print("\n\nFim do jogo!")
        break  

jogar()
