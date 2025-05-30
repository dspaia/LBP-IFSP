import random

class Navio:
    def __init__ (self, tamanho, coordenadas):
        self.tamanho = tamanho
        self.coordenadas = coordenadas
        self.acertos = set()

    def foi_afundado(self):
        return len(self.acertos) == self.tamanho
    
    def verificar_tiro(self, tiro):
        if tiro in self.coordenadas:
            self.acertos.add(tiro)
            return True
        return False

class Tabuleiro:
    def __init__(self, tamanho = 10):
        self.tamanho = tamanho
        self.grid = [['~' for _ in range(tamanho)] for _ in range (tamanho)]
        self.navios = []

    def pode_posicionar(self, coordenadas):
        for(x, y) in coordenadas:
            if not (0 <= x < self.tamanho and 0 <= y < self.tamanho):
                return False
            if self.grid[x][y] == 'N':
                return False
        return True
    
    def posicionar_navio(self, navio):
        self.navios.append(navio)
        for (x, y) in navio.coordenadas:
            self.grid[x][y] = 'N'

    def receber_tiro(self, x, y):
        if self.grid[x][y] in ['X', 'O']:
            return "Esse local já foi atingido."
        for navio in self.navios:
            if navio.verificar_tiro((x,y)):
                self.grid[x][y]= 'X'
                if navio.foi_afundado():
                    return "Afundou um navio!"
                else:
                    return "Acertou!"
                
        self.grid[x][y] = 'O'
        return "Água!"
    
    def todos_afundados(self):
        return all(navio.foi_afundado() for navio in self.navios)
    
    def exibir(self, revelar_navios = False):

        cabecalho = ("  " + " ".join(str(i) for i in range(self.tamanho)))
        print(cabecalho)

        for i in range(self.tamanho):
            linha = []
            for j in range(self.tamanho):
                if self.grid[i][j] == 'N' and not revelar_navios:
                    linha.append('.')
                else:
                    linha.append(self.grid[i][j])
            print(f"{i:2} " + " ".join(linha))
        print()

def gerar_coordenadas(tamanho, xinicio, xfim, yinicio, yfim):
    coordenadas = []
    if xinicio == xfim:
        inicio, fim = sorted([yinicio, yfim])
        if fim - inicio + 1 != tamanho:
            return None
        coordenadas = [(xinicio, y) for y in range(inicio, fim+1)]
    elif yinicio == yfim:
        inicio, fim = sorted([xinicio, xfim])
        if fim - inicio + 1 != tamanho:
            return None
        coordenadas = [(x, yinicio) for x in range(inicio, fim + 1)]
    else:
        return None
    return coordenadas

def posicionar_navios_manualmente(tabuleiro, informacoes_navios):
    print("--POSICIONE SEUS NAVIOS NO TABULEIRO--")
    for nome, tamanho in informacoes_navios.items():
        while True:
            tabuleiro.exibir(revelar_navios=True)
            print(f"Posicione seu {nome} (tamanho: {tamanho})")
            try:
                xinicio = int(input(f"Linha inicial (0-{tabuleiro.tamanho - 1}): "))
                yinicio = int(input(f"Coluna inicial (0-{tabuleiro.tamanho - 1}): "))
                xfim = int(input(f"Linha final (0-{tabuleiro.tamanho - 1}): "))
                yfim = int(input(f"Coluna final (0-{tabuleiro.tamanho - 1}): "))
            except ValueError:
                print("Tente usar números para posicionar seu navio.")
                continue
            coordenadas = gerar_coordenadas(tamanho, xinicio, xfim, yinicio, yfim)
            if coordenadas is None:
                print("Não foi possível posicionar seu navio. O posicionamento deve ser reto e condizente com o tamanho do navio.")
                continue
            if not tabuleiro.pode_posicionar(coordenadas):
                print("A posição está ocupada ou não está dentro do tabuleiro. Tente de novo.")
                continue
            navio = Navio(tamanho, coordenadas)
            tabuleiro.posicionar_navio(navio)
            tabuleiro.exibir(revelar_navios=True)
            break

def posicionar_navios_automatico(tabuleiro, informacoes_navios):
    for nome, tamanho in informacoes_navios.items():
        while True:
            horizontal = random.choice([True, False])
            if horizontal:
                x = random.randint(0, tabuleiro.tamanho-1)
                y = random.randint(0, tabuleiro.tamanho-tamanho)
                coordenadas = [(x,y + i) for i in range (tamanho)]
            else:
                x = random.randint(0, tabuleiro.tamanho - tamanho)
                y = random.randint(0, tabuleiro.tamanho - 1)
                coordenadas = [(x + i, y) for i in range(tamanho)]
            if tabuleiro.pode_posicionar(coordenadas):
                navio = Navio(tamanho, coordenadas)
                tabuleiro.posicionar_navio(navio)
                break

def solicitar_jogada (tabuleiro_ataque):
    while True:
        try:
            x = int(input(f"Digite a linha para atacar (0 - {tabuleiro_ataque.tamanho - 1}): "))
            y = int(input(f"Digite a coluna para atacar (0 - {tabuleiro_ataque.tamanho - 1}): "))
        except ValueError:
            print("Números inválidos. Digite números válidos.")
            continue
        if not (0 <= x < tabuleiro_ataque.tamanho and 0 <= y < tabuleiro_ataque.tamanho):
            print("Essas coordenadas não estão no tabuleiro.")
            continue
        if tabuleiro_ataque.grid[x][y] in ['X', 'O']:
            print("Você já atirou nessa posição.")
            continue
        return x, y

def jogada_computador(tabuleiro_jogador, tiros_feitos):
    while True:
        x = random.randint(0, tabuleiro_jogador.tamanho-1)
        y = random.randint(0, tabuleiro_jogador.tamanho-1)
        if (x,y) not in tiros_feitos:
            tiros_feitos.add((x,y))
            return x, y
        
def main():
    while True:
        informacoes_navios = {
            "destroier": 2,
            "cruzador": 3,
            "submarino": 3,
            "encouraçado": 4,
            "porta-aviões": 5
        }

        tabuleiro_jogador = Tabuleiro()
        tabuleiro_computador = Tabuleiro()
        tabuleiro_ataque = Tabuleiro()

        posicionar_navios_manualmente(tabuleiro_jogador, informacoes_navios)
        posicionar_navios_automatico(tabuleiro_computador, informacoes_navios)

        tiros_computador = set()
        print("\n---Que comece a batalha!---")
        while True:
            print("--------------------\nSeu tabuleiro:")
            tabuleiro_jogador.exibir(revelar_navios = True)
            print("--------------------\nSeu tabuleiro de ataque:")
            tabuleiro_ataque.exibir()

            print("Sua vez!")
            x, y = solicitar_jogada(tabuleiro_ataque)
            resultado = tabuleiro_computador.receber_tiro(x,y)
            print(resultado)

            if tabuleiro_ataque.grid[x][y] not in ['X', 'O']:
                tabuleiro_ataque.grid[x][y] = 'X' if resultado in ["Acertou!", "Afundou um navio!"] else 'O'
            if tabuleiro_computador.todos_afundados():
                print("Parabéns! Você conseguiu afundar todos os navios do seu adversário! Você venceu!")
                break

            print("Vez do seu oponente")
            x, y = jogada_computador(tabuleiro_jogador, tiros_computador)
            resultado = tabuleiro_jogador.receber_tiro(x, y)
            print(f"Seu oponente atirou em ({x}, {y}) e {resultado}")
            if tabuleiro_jogador.todos_afundados():
                print("Seu oponente afundou todos os seus navios, que droga! Você perdeu.")
                break

        jogar_novamente = input("Jogar novamente? (s/n): ").strip().lower()
        if jogar_novamente != "s":
            print("Obrigado por jogar, até a próxima!")
            break

if __name__ == "__main__":
    main()