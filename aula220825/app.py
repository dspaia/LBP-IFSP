from flask import Flask, render_template, jsonify
from flask import json


app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo_pagina = "Início - LaEli vros", pagina_ativa = 'index')


@app.route('/base')
def base():
    return render_template('base.html', )

@app.route('/livros')
def livros():
    return render_template('livros.html', titulo_pagina="Biblioteca - LaEli vros", pagina_ativa='livros')


@app.route('/api/livros')
def api_livros():
    livros = [
        {
            "id": 1,
            "titulo": "Recursão",
            "autor": "Blake Crounch",
            "avaliacao": 5,
            "descricao": "Pra fritar o cérebro até sair pela boca.",
            "genero": "Ficção Científica",
            "paginas": 320,
            "imagem": "/static/imagens/recursao_capa.jpg",
            "link": "/recursao"
        },

        {
            "id": 2,
            "titulo": "Tudo é Rio",
            "autor": "Carla Madeira",
            "avaliacao": 5,
            "descricao": "Pra cair as prega do cu de tão 'socorro'.",
            "genero": "Romance de amor (ou não)",
            "paginas": 210,
            "imagem": "/static/imagens/tudoerio_capa.jpg",
            "link": "/tudoerio"
        },

        {
            "id": 3,
            "titulo": "Uma Família Feliz",
            "autor": "Raphael Montes",
            "avaliacao": 5,
            "descricao": "Para você ficar fudido mentalmente rs.",
            "genero": "Drama",
            "paginas": 352,
            "imagem": "/static/imagens/umafamiliafeliz_capa.jpg",
            "link": "/umafamiliafeliz"
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