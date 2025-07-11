import random
from flask import Flask, session, request, jsonify, send_from_directory

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
    session['acerto'] = random.randint(1, 100)
    session['tentativas'] = 0
    return jsonify({'mensagem': 'Novo jogo iniciado!'})

@app.route('/api/palpite', methods=['POST'])
def palpite():
    data = request.get_json()
    palpite = int(data.get('palpite', 0))
    acerto = session.get('acerto')
    tentativas = session.get('tentativas', 0) + 1
    session['tentativas'] = tentativas

    if palpite == acerto:
        resposta = {
            'resultado': 'acertou',
            'mensagem': f'Parabéns, você acertou! O número era: {acerto}.',
            'tentativas': tentativas
        }
        # Reinicia o jogo automaticamente ou aguarda nova chamada para /api/iniciar
    elif palpite < acerto:
        resposta = {
            'resultado': 'menor',
            'mensagem': f'O número {palpite} é menor que o número a ser adivinhado.',
            'tentativas': tentativas
        }
    else:
        resposta = {
            'resultado': 'maior',
            'mensagem': f'O número {palpite} é maior que o número a ser adivinhado.',
            'tentativas': tentativas
        }
    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True)