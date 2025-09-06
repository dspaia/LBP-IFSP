from flask import Flask, render_template, jsonify
from flask import json


app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo_pagina = "Início - LaEli vros", pagina_ativa = 'index')


@app.route('/base')
def base():
    return render_template('base.html', )

@app.route('/api/livros')
def api_livros():
    livros = [
        {
        "id": 1,
        "conteudo": '''
        <div class="livro-detalhes">
            <div class="capa">
                <img src="/static/imagens/recursao_capa.jpg" alt="Recursão">
            </div>
            <div class="informacoes">
                <h2>Recursão</h2>
                <p><strong>Autor:</strong> Blake Crounch</p>
                <p><strong>Avaliação:</strong> ⭐⭐⭐⭐⭐ (5/5)</p>
                <p><strong>Descrição:</strong> Pra fritar o cérebro até sair pela boca.</p>
                <p><strong>Gênero:</strong> Ficção Científica</p>
                <p><strong>Páginas:</strong> 320</p>
            </div>
        </div>
        '''
},

        {
        'id': 2,
         'conteudo': '''
        <div class="livro-detalhes">
            <div class="capa">
                <img src="{{ url_for('static', filename='imagens/tudoerio_capa.jpg') }}" alt="Tudo é Rio">
            </div>

            <div class="informacoes">
                <h2>Recursão</h2>
                <p><strong>Autor:</strong> Carla Madeira</p>
                <p><strong>Avaliação:</strong> ⭐⭐⭐⭐⭐ (5/5)</p>
                <p><strong>Descrição:</strong> Pra cair as prega do cu de tão 'socorro'.</p>
                <p><strong>Gênero:</strong> Romance de amor (ou não)</p>
                <p><strong>Páginas:</strong> 210</p>
            </div>
        </div>''' 
},

        {'id': 3,
         'conteudo': '''
        <div class="livro-detalhes">
            <div class="capa">
                <img src="{{ url_for('static', filename='imagens/umafamiliafeliz_capa.jpg') }}" alt="Uma Família Feliz">
            </div>

            <div class="informacoes">
                <h2>Uma Família Feliz</h2>
                <p><strong>Autor:</strong> Tati Bernardi</p>
                <p><strong>Avaliação:</strong> ⭐⭐⭐⭐⭐ (5/5)</p>
                <p><strong>Descrição:</strong> Pra rir, chorar e refletir sobre a vida.</p>
                <p><strong>Gênero:</strong> Romance contemporâneo</p>
                <p><strong>Páginas:</strong> 256</p>
            </div>
        </div>''' 
}
    ]
    return jsonify(livros)

#Livro
@app.route('/recursao')
def recursao():
    return render_template('recursao.html', titulo_pagina = "Recursao - LaEli vros", pagina_ativa = 'livro')

#Livro
@app.route('/tudoerio')
def tudoerio():
    return render_template('tudoerio.html', titulo_pagina = "Tudo e rio - LaEli vros", pagina_ativa = 'livro')

#Livro
@app.route('/umafamiliafeliz')
def umafamiliafeliz():
    return render_template('umafamiliafeliz.html', titulo_pagina = "Uma familia feliz - LaEli vros", pagina_ativa = 'livro')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo_pagina = "Sobre - LaEli vros", pagina_ativa = 'sobre')

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo_pagina = "Contato - LaEli vros", pagina_ativa = 'contato')

if __name__ == '__main__':
    app.run (debug=True)