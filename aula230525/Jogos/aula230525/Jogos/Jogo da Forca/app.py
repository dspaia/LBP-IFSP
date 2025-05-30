import random

class Palavra:
    def __init__(self, nome, tema):
        self.nome = nome.lower()
        self.tema = tema
        self.letras_descobertas = ['_' for _ in self.nome]
    
    def verificar_letra(self, letra_escolhida):
        acertou = False
        for i, letra in enumerate(self.nome):
            if letra == letra_escolhida:
                self.letras_descobertas[i] = letra
                acertou = True
        return acertou
    
    def palavra_completa(self):
        return ''.join(self.letras_descobertas)

    def terminou(self):
        return '_' not in self.letras_descobertas

    def exibir_progresso(self):
        print(' '.join(self.letras_descobertas))
        
palavras = [
    Palavra("curupira", "Folclore Brasileiro"),
    Palavra("uirapuru", "Folclore Brasileiro"),
    Palavra("lasanha", "Comida"),
    Palavra("bacalhau", "Comida"),
    Palavra("cebolinha", "Personagem"),
    Palavra("magali", "Personagem"),
    Palavra("ornitorrinco", "Animal"),
    Palavra("guepardo", "Animal"),
    Palavra("espanha", "País"),
    Palavra("alemanha", "País")
]

palavras_jogadas = []

while True:
    palavras_restantes = [p for p in palavras if p.nome not in palavras_jogadas]

    if not palavras_restantes:
        print("\n✅ Você jogou todas as palavras disponíveis. Fim do jogo!")
        break

    palavra = random.choice(palavras_restantes)
    palavras_jogadas.append(palavra.nome)

    tentativas_restantes = 6
    letras_erradas = []

    print("====JOGO DA FORCA====")
    print(f"----------------\nTema: {palavra.tema}")

    while tentativas_restantes > 0 and not palavra.terminou():
        print(f"\nPalavra:")
        palavra.exibir_progresso()
        print(f"\nErros: {' '.join(letras_erradas)}")
        print(f"Tentativas restantes: {tentativas_restantes}\n----------------")

        letra = input("Digite uma letra ou ! para dar um palpite: ").lower().strip()

        if letra == "!":
            palpite = input("Digite seu palpite: ")
            if palpite == palavra.nome:
                print(f"------------------\nParabéns! Você acertou a palavra: {palavra.nome.upper()}")
                break
            else:
                print(f"Palpite incorreto!")
                tentativas_restantes -= 1

        if len(letra) != 1 or not letra.isalpha() and letra != "!":
            print("Digite apenas uma letra!")
            continue
        
        if letra in palavra.letras_descobertas or letra in letras_erradas:
            print("Você já tentou essa letra!")
            continue

        if palavra.verificar_letra(letra):
            print("Esta letra está presente na palavra!")
        elif letra != "!":
            print("Esta letra não está presente na palavra!")
            letras_erradas.append(letra)
            tentativas_restantes -= 1

    if palavra.terminou():
        print(f"------------------\nParabéns! Você acertou a palavra: {palavra.nome.upper()}")
    else:
        print(f"------------------\nFim de jogo! A palavra era: {palavra.nome.upper()}")

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower().strip()
    if jogar_novamente != 's':
        print("Obrigado por jogar!")
        break