class Disco:
    def __init__(self, nome, cor, tamanho):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho

class Poste:
    def __init__(self, nome):
        self.nome = nome
        self.discos = list()

    def adicionar_disco(self, disco):
        self.discos.append(disco)

    def exibir_detalhes(self):
        print(f"Poste {self.nome}: ", end=" ")
        if self.discos:
            for disco in reversed(self.discos):
                print(f" Disco {disco.tamanho}", end=", ")
        else:
            print("Nenhum disco")
        print()
    
    def mover_disco(self, poste_destino):
        if not self.discos:
            print(f"Não há discos para mover no poste {self.nome}")
            return False
        
        disco = self.discos[-1]
        if poste_destino.discos and disco.tamanho > poste_destino.discos[-1].tamanho:
            print("Não é permitido colocar um disco maior sobre um menor.")
            return False
            
        self.discos.pop()
        poste_destino.adicionar_disco(disco)
        print(f"Movido disco {disco.tamanho} do poste {self.nome} para o poste {poste_destino.nome}.") 
        return True

discos = [
    Disco("n5", "", 5),
    Disco("n4", "", 4),
    Disco("n3", "", 3),
    Disco("n2", "", 2),
    Disco("n1", "", 1)
]

postes = [Poste("A"), Poste("B"), Poste("C")]
for disco in discos:
    postes[0].adicionar_disco(disco)

mapa_postes = {poste.nome: poste for poste in postes}

contagem = 0

while True:
    print("\n===== Torre de Hanoi =====\n")
    for poste in postes:
        poste.exibir_detalhes()

    origem_input = input("Mover de qual poste (A/B/C)? ").strip().upper()
    destino_input = input("Mover para qual poste (A/B/C)? ").strip().upper()

    origem = mapa_postes.get(origem_input)
    destino = mapa_postes.get(destino_input)

    if origem and destino:
        if origem.mover_disco(destino):
            contagem += 1
            print(f"Movimentos: {contagem}")
    else:
        print("Poste inválido. Tente novamente com A, B ou C.")

    if len(postes[2].discos) == len(discos):
        print("\nParabéns! Você completou a Torre de Hanoi!")
        break
        