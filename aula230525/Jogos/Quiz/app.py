import random
from flask import Flask, session, request, jsonify, send_from_directory

class Pergunta:
    def __init__(self, pergunta, resposta, alternativa1, alternativa2, alternativa3, alternativa4):
        self.pergunta = pergunta
        self.resposta = resposta
        self.alternativas = [alternativa1, alternativa2, alternativa3, alternativa4]

    def embaralhar_alternativas(self):
        alternativas_embaralhadas = self.alternativas[:]
        random.shuffle(alternativas_embaralhadas)
        letras = ['a', 'b', 'c', 'd']
        mapa = dict(zip(letras, alternativas_embaralhadas))
        letra_correta = [letra for letra, alt in mapa.items() if alt == self.resposta][0]
        return mapa, letra_correta

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
    session['indice'] = 0
    session['pontuacao'] = 0
    session['ordem'] = random.sample(range(len(perguntas)), len(perguntas))
    return proxima_pergunta()

def proxima_pergunta():
    indice = session.get('indice', 0)
    ordem = session.get('ordem', list(range(len(perguntas))))
    if indice >= len(perguntas):
        return jsonify({
            'fim': True,
            'pontuacao': session.get('pontuacao', 0),
            'total': len(perguntas)
        })
    pergunta_obj = perguntas[ordem[indice]]
    mapa, _ = pergunta_obj.embaralhar_alternativas()
    session['mapa'] = mapa
    session['resposta_correta'] = [letra for letra, alt in mapa.items() if alt == pergunta_obj.resposta][0]
    return jsonify({
        'fim': False,
        'pergunta': pergunta_obj.pergunta,
        'alternativas': mapa,
        'indice': indice + 1,
        'total': len(perguntas)
    })

@app.route('/api/responder', methods=['POST'])
def responder():
    data = request.get_json()
    alternativa = data.get('alternativa')
    resposta_correta = session.get('resposta_correta')
    pontuacao = session.get('pontuacao', 0)
    correta = alternativa == resposta_correta
    if correta:
        pontuacao += 1
        session['pontuacao'] = pontuacao
    session['indice'] = session.get('indice', 0) + 1
    return jsonify({
        'correta': correta,
        'resposta_correta': resposta_correta,
        'pontuacao': pontuacao,
        'proxima': proxima_pergunta().json
    })

if __name__ == '__main__':
    app.run(debug=True)