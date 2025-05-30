import random

opcoes = ["pedra", "papel", "tesoura"]
pontuacao_jogador = 0
pontuacao_computador = 0

while True:
    print(f"--------Jokenpô!--------\n")
    tipo_jogo = int(input("Quer definir um número de partidas (DIGITE 1) ou jogar até quando quiser (DIGITE 2)? "))
        
    if tipo_jogo == 1:
        partidas = int(input("------------------\nQuantas partidas um dos jogadores precisa ganhar para o jogo terminar? "))

        while pontuacao_computador < partidas and pontuacao_jogador < partidas:
            escolha = input("------------------\nFaça sua escolha. Pedra, papel ou tesoura? ").lower()
            if escolha not in opcoes:
                print("Escolha inválida. Tente novamente.")
                continue

            computador = random.choice(opcoes)

            print(f"------------------\nVocê escolheu {escolha}.")
            print(f"Seu oponente escolheu {computador}.")

            if escolha == computador:
                print(f"------------------\nEmpate! Ambos escolheram {escolha}\nSua pontuação: {pontuacao_jogador}\nPontuação do adversário: {pontuacao_computador}")
            elif (escolha == "tesoura" and computador == "papel") or (escolha == "papel" and computador == "pedra") or (escolha == "pedra" and computador == "tesoura"):
                pontuacao_jogador += 1
                print(f"------------------\nVocê venceu, já que escolheu {escolha} e seu oponente escolheu {computador}.\nSua pontuação: {pontuacao_jogador}\nPontuação do adversário: {pontuacao_computador}")
            else:
                pontuacao_computador += 1
                print(f"------------------\nSeu oponente venceu, já que ele escolheu {computador} e você escolheu {escolha}.\nSua pontuação: {pontuacao_jogador}\nPontuação do adversário: {pontuacao_computador}")
                
        if pontuacao_jogador == partidas:
            print(f"------------------\nParabéns, jogador! Você venceu com {pontuacao_jogador} e seu oponente perdeu com {pontuacao_computador}")
        elif pontuacao_computador == partidas:
            print(f"------------------\nQue droga! Você perdeu com {pontuacao_jogador} e seu oponente venceu com {pontuacao_computador}")
        novamente = input("------------------\nQuer jogar de novo? SIM ou NÃO? ")
        if novamente != "sim":
            print("Até a próxima!") 
            break
        else:
            pontuacao_computador = 0
            pontuacao_jogador = 0

    elif tipo_jogo == 2:
        while True:
            escolha = input("------------------\nFaça sua escolha. Pedra, papel ou tesoura? ").lower()
            if escolha not in opcoes:
                print("Escolha inválida. Tente novamente.")
                continue

            computador = random.choice(opcoes)

            print(f"------------------\nVocê escolheu {escolha}.")
            print(f"Seu oponente escolheu {computador}.")

            if escolha == computador:
                print(f"------------------\nEmpate! Ambos escolheram {escolha}.")
            elif (escolha == "tesoura" and computador == "papel") or (escolha == "papel" and computador == "pedra") or (escolha == "pedra" and computador == "tesoura"):
                print(f"------------------\nVocê venceu, já que escolheu {escolha} e seu oponente escolheu {computador}.")
            else:
                print(f"------------------\nSeu oponente venceu, já que ele escolheu {computador} e você escolheu {escolha}.")

            novamente = input("------------------\nQuer jogar de novo? SIM ou NÃO? ")
            if novamente != "sim":
                print("Até a próxima!") 
                break
            else:
                pontuacao_computador = 0
                pontuacao_jogador = 0