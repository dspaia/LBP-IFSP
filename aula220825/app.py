from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html', titulo_pagina = "Início - LaEli vros", pagina_ativa = 'index')


@app.route('/base')
def base():
    return render_template('base.html', )

@app.route('/livros')
def livros():
    return render_template('livros.html', titulo_pagina = "Livros - LaEli vros", pagina_ativa = 'biblioteca')

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