from flask import Flask, session, request, jsonify, send_from_directory

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

    def mover_disco(self, poste_destino):
        if not self.discos:
            return False, "Não há discos para mover."
        disco = self.discos[-1]
        if poste_destino.discos and disco.tamanho > poste_destino.discos[-1].tamanho:
            return False, "Não é permitido colocar um disco maior sobre um menor."
        self.discos.pop()
        poste_destino.adicionar_disco(disco)
        return True, f"Movido disco {disco.tamanho} do poste {self.nome} para o poste {poste_destino.nome}."

def criar_jogo():
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
    return postes

def serializar_postes(postes):
    return [
        {
            'nome': poste.nome,
            'discos': [disco.tamanho for disco in poste.discos]
        }
        for poste in postes
    ]

def desserializar_postes(data):
    postes = [Poste("A"), Poste("B"), Poste("C")]
    for i, poste_data in enumerate(data):
        postes[i].discos = [Disco(f"n{t}", "", t) for t in poste_data['discos']]
    return postes

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
    postes = criar_jogo()
    session['postes'] = serializar_postes(postes)
    session['contagem'] = 0
    return jsonify({
        'postes': session['postes'],
        'contagem': session['contagem']
    })

@app.route('/api/mover', methods=['POST'])
def mover():
    data = request.get_json()
    origem_nome = data.get('origem')
    destino_nome = data.get('destino')
    postes = desserializar_postes(session.get('postes'))
    mapa_postes = {poste.nome: poste for poste in postes}
    origem = mapa_postes.get(origem_nome)
    destino = mapa_postes.get(destino_nome)
    if origem and destino:
        sucesso, mensagem = origem.mover_disco(destino)
        if sucesso:
            session['contagem'] = session.get('contagem', 0) + 1
            session['postes'] = serializar_postes(postes)
            venceu = len(mapa_postes['C'].discos) == 5
            return jsonify({
                'sucesso': True,
                'mensagem': mensagem,
                'postes': session['postes'],
                'contagem': session['contagem'],
                'venceu': venceu
            })
        else:
            return jsonify({'sucesso': False, 'mensagem': mensagem}), 400
    else:
        return jsonify({'sucesso': False, 'mensagem': 'Poste inválido.'}), 400

if __name__ == '__main__':
    app.run(debug=True)