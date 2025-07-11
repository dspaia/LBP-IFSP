import random
from flask import Flask, session, request, jsonify, send_from_directory

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

def jogada_computador(tabuleiro_jogador, tiros_feitos):
    while True:
        x = random.randint(0, tabuleiro_jogador.tamanho-1)
        y = random.randint(0, tabuleiro_jogador.tamanho-1)
        if (x,y) not in tiros_feitos:
            tiros_feitos.add((x,y))
            return x, y

app = Flask(__name__, static_folder='site', template_folder='site')
app.secret_key = 'sua_chave_secreta'  # Troque por uma chave segura

@app.route('/')
def index():
    return send_from_directory('site', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('site', filename)

@app.route('/api/iniciar', methods=['POST'])
def iniciar():
    informacoes_navios = {
        "destroier": 2,
        "cruzador": 3,
        "submarino": 3,
        "encouraçado": 4,
        "porta-aviões": 5
    }
    tabuleiro_jogador = Tabuleiro()
    tabuleiro_computador = Tabuleiro()
    posicionar_navios_automatico(tabuleiro_jogador, informacoes_navios)
    posicionar_navios_automatico(tabuleiro_computador, informacoes_navios)
    session['tabuleiro_jogador'] = [[cell for cell in row] for row in tabuleiro_jogador.grid]
    session['tabuleiro_computador'] = [[cell for cell in row] for row in tabuleiro_computador.grid]
    session['tiros_computador'] = []
    return jsonify({'mensagem': 'Novo jogo iniciado!'})

@app.route('/api/tiro', methods=['POST'])
def tiro():
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')
    grid_computador = session.get('tabuleiro_computador')
    grid_ataque = session.get('tabuleiro_jogador')
    if grid_computador is None or grid_ataque is None:
        return jsonify({'erro': 'Jogo não iniciado.'}), 400
    resultado = ""
    if grid_computador[x][y] in ['X', 'O']:
        resultado = "Esse local já foi atingido."
    elif grid_computador[x][y] == 'N':
        grid_computador[x][y] = 'X'
        resultado = "Acertou!"
    else:
        grid_computador[x][y] = 'O'
        resultado = "Água!"
    session['tabuleiro_computador'] = grid_computador
    return jsonify({'resultado': resultado})

@app.route('/api/estado', methods=['GET'])
def estado():
    grid_jogador = session.get('tabuleiro_jogador')
    grid_computador = session.get('tabuleiro_computador')
    if grid_jogador is None or grid_computador is None:
        return jsonify({'erro': 'Jogo não iniciado.'}), 400
    return jsonify({
        'tabuleiro_jogador': grid_jogador,
        'tabuleiro_computador': grid_computador
    })

@app.route('/api/sair', methods=['POST'])
def sair():
    session.clear()
    return jsonify({'mensagem': 'Sessão encerrada.'})

if __name__ == "__main__":
    app.run(debug=True)