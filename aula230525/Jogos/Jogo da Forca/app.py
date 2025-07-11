import random
from flask import Flask, session, request, jsonify, send_from_directory

class Palavra:
    def __init__(self, nome, tema):
        self.nome = nome.lower()
        self.tema = tema

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
    palavra = random.choice(palavras)
    session['palavra'] = palavra.nome
    session['tema'] = palavra.tema
    session['letras_descobertas'] = ['_' for _ in palavra.nome]
    session['tentativas_restantes'] = 6
    session['letras_erradas'] = []
    return jsonify({
        'tema': palavra.tema,
        'letras_descobertas': session['letras_descobertas'],
        'tentativas_restantes': session['tentativas_restantes'],
        'letras_erradas': session['letras_erradas']
    })

@app.route('/api/tentar', methods=['POST'])
def tentar():
    data = request.get_json()
    letra = data.get('letra', '').lower()
    palavra_nome = session.get('palavra')
    letras_descobertas = session.get('letras_descobertas')
    tentativas_restantes = session.get('tentativas_restantes')
    letras_erradas = session.get('letras_erradas')

    if not palavra_nome or not letras_descobertas:
        return jsonify({'erro': 'Jogo não iniciado.'}), 400

    acertou = False
    for i, letra_palavra in enumerate(palavra_nome):
        if letra_palavra == letra:
            letras_descobertas[i] = letra
            acertou = True

    if not acertou:
        if letra not in letras_erradas:
            letras_erradas.append(letra)
            tentativas_restantes -= 1

    session['letras_descobertas'] = letras_descobertas
    session['tentativas_restantes'] = tentativas_restantes
    session['letras_erradas'] = letras_erradas

    terminou = '_' not in letras_descobertas
    return jsonify({
        'letras_descobertas': letras_descobertas,
        'tentativas_restantes': tentativas_restantes,
        'letras_erradas': letras_erradas,
        'terminou': terminou,
        'palavra': palavra_nome if terminou or tentativas_restantes == 0 else None
    })

if __name__ == '__main__':
    app.run(debug=True)