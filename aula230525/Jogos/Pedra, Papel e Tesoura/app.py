import random
from flask import Flask, session, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='site', template_folder='site')
app.secret_key = 'sua_chave_secreta'  # Troque por uma chave segura

opcoes = ["pedra", "papel", "tesoura"]

@app.route('/')
def index():
    return send_from_directory('site', 'index.html')

@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory('site', filename)

@app.route('/api/iniciar', methods=['POST'])
def iniciar():
    session['pontuacao_jogador'] = 0
    session['pontuacao_computador'] = 0
    partidas = request.get_json().get('partidas')
    session['partidas'] = partidas if partidas else None
    return jsonify({
        'mensagem': 'Novo jogo iniciado!',
        'partidas': session['partidas'],
        'pontuacao_jogador': session['pontuacao_jogador'],
        'pontuacao_computador': session['pontuacao_computador']
    })

@app.route('/api/jogar', methods=['POST'])
def jogar():
    data = request.get_json()
    escolha = data.get('escolha')
    if escolha not in opcoes:
        return jsonify({'erro': 'Escolha inválida.'}), 400

    computador = random.choice(opcoes)
    pontuacao_jogador = session.get('pontuacao_jogador', 0)
    pontuacao_computador = session.get('pontuacao_computador', 0)
    partidas = session.get('partidas')

    if escolha == computador:
        resultado = 'empate'
    elif (escolha == "tesoura" and computador == "papel") or \
         (escolha == "papel" and computador == "pedra") or \
         (escolha == "pedra" and computador == "tesoura"):
        resultado = 'vitoria'
        pontuacao_jogador += 1
    else:
        resultado = 'derrota'
        pontuacao_computador += 1

    session['pontuacao_jogador'] = pontuacao_jogador
    session['pontuacao_computador'] = pontuacao_computador

    terminou = False
    vencedor = None
    if partidas:
        if pontuacao_jogador == partidas:
            terminou = True
            vencedor = 'jogador'
        elif pontuacao_computador == partidas:
            terminou = True
            vencedor = 'computador'

    return jsonify({
        'escolha_jogador': escolha,
        'escolha_computador': computador,
        'resultado': resultado,
        'pontuacao_jogador': pontuacao_jogador,
        'pontuacao_computador': pontuacao_computador,
        'terminou': terminou,
        'vencedor': vencedor
    })

if __name__ == '__main__':
    app.run(debug=True)