import random

num_min = 1
num_max = 100
acerto = random.randint(1, 100)
tentativas = 0
palpite = 0

print("------Adivinhe o número!------")

while True:
    palpite = int(input("Palpite (1 a 100): "))
    tentativas += 1
    if palpite == acerto:
        print(f"Parabéns, você acertou! O número era: {acerto}.\nNúmero de tentativas necessárias: {tentativas}\n" + "-" * 30)
        sim_nao = input("Jogar novamente? SIM ou NÃO? ").lower()
        if sim_nao != "sim":
            print("Até a próxima!")
            break
        else:
            acerto = random.randint(1,100)
            tentativas = 0
    elif palpite < acerto:
        print(f"Quase lá! O número {palpite} é menor que o número a ser adivinhado.\nNúmero de tentativas: {tentativas}\n" + "-" * 30)
    elif palpite > acerto:
        print(f"Quase lá! O número {palpite} é maior que o número a ser adivinhado.\nNúmero de tentativas: {tentativas}\n" + "-" * 30)