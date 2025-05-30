import random

class Pergunta:
    def __init__(self, pergunta, resposta, alternativa1, alternativa2, alternativa3, alternativa4):
        self.pergunta = pergunta
        self.resposta = resposta
        self.alternativas = [alternativa1, alternativa2, alternativa3, alternativa4]
    
    def exibir_pergunta(self):
        print(f"-----------------------\nPergunta: {self.pergunta}\n")

        alternativas_embaralhadas = self.alternativas[:]
        random.shuffle(alternativas_embaralhadas)

        letras = ['a', 'b', 'c', 'd']
        self.mapa_alternativas = dict(zip(letras, alternativas_embaralhadas))

        for letra, alternativa in self.mapa_alternativas.items():
            if alternativa == self.resposta:
                self.letra_correta = letra
                break

        for letra in letras:
            print(f"{letra}) {self.mapa_alternativas[letra]}")

    def verificar_resposta(self, alternativa_escolhida, pontuacao):
        if alternativa_escolhida == self.letra_correta:
            pontuacao += 1
            print(f"--------------------------\nCerta resposta!\nResposta correta: {self.resposta}\nPontuação: {pontuacao}")
        else:
            print(f"--------------------------\nResposta errada!\nResposta correta: {self.letra_correta}: {self.resposta}\nPontuação: {pontuacao}") 
        return pontuacao

perguntas = [
    Pergunta("1- Qual o nome da terra governada por Odisseu?", "Ítaca", "Tróia", "Grécia", "Ítaca", "Roma"),
    Pergunta("2- Quantos anos Odisseu ficou na Guerra de Tróia?", "10", "10", "4", "7", "15"),
    Pergunta("3- Quem abriu a bolsa de vento dada pelo deus Éolo e fez com que os guerreiros ficassem mais longe de casa?", "Euríloco", "Polites", "Menelau", "Euríloco", "Odisseu"),
    Pergunta("4- Qual deusa era mentora de Odisseu?", "Atena", "Hera", "Atena", "Deméter", "Ártemis"),
    Pergunta("5- Qual o desafio que Penélope propôs para que disputassem pelo trono?", "Usando o arco de seu marido, atirar em um alvo através de 12 machados.", "Crochetar uma manta com fios de ouro primeiro que todos os outros.", "Lutar com os olhos vendados com três dos melhores guerreiros do reino.", "Fazer um quadro realista da rainha, que seria julgado pelas suas cinco damas de companhia.", "Usando o arco de seu marido, atirar em um alvo através de 12 machados."), 
    Pergunta("6- Qual o nome do monstro que devora exatamente seis homens de Odisseu?", "Scylla", "Polifêmo", "Charybids", "Cérbero", "Scylla"),
    Pergunta("7- Qual o maior inimigo de Odisseu?", "Poseidon", "Hermes", "Zeus", "Poseidon", "Ares"),
    Pergunta("8- Em que criatura Circe transforma os homens de Odisseu quando os captura?", "Porcos", "Porcos", "Galinhas", "Sapos", "Vacas"),
    Pergunta("9- Onde está o profeta que Odisseu precisa encontrar para voltar para casa?", "Submundo", "Ítaca", "Olimpo", "Tróia", "Submundo"),
    Pergunta("10- Qual o desafio que Penélope propõe à Odisseu para provar que ele ainda é seu marido?", "Ela diz para ele mover a cama dos dois, que foi entalhada na árvore em que eles se conheceram.", "Ela pede para Odisseu esticar seu arco, que só ele consegue esticar.", "Ela traz amigos de Odisseu para reconhecê-lo e fazer perguntas sobre sua vida.", "Ela diz para ele mover a cama dos dois, que foi entalhada na árvore em que eles se conheceram.", "Ela não propõe nenhum desafio.")
]

pontuacao = 0

print(f"-------QUIZ ODISSEIA-------")

for pergunta in perguntas:
    pergunta.exibir_pergunta()
    resposta = input("Resposta (a, b, c, d): ").strip().lower()
    while resposta not in ["a", "b", "c", "d"]:
        resposta = input("Entrada inválida, digite uma das letras (a, b, c, d): ")
    pontuacao = pergunta.verificar_resposta(resposta, pontuacao)

print(f"-----------------------------\n🎉 Fim do quiz! Sua pontuação final foi {pontuacao} de {len(perguntas)}.")