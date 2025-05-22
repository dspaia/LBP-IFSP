from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'segredo123'

@app.route('/')
def formulario():
    return render_template('site_formulario.html')

@app.route('/salvar', methods=['POST'])
def salvar():
    session['nome'] = request.form['nome']
    session['idade'] = request.form['idade']
    session['email'] = request.form['email']
    return redirect('/dados_salvos')

@app.route('/dados_salvos')
def dados_salvos():
    return render_template('dados_salvos.html')

@app.route('/exibir')
def exibir():
    nome = session.get('nome')
    idade = session.get('idade')
    email = session.get('email')
    return render_template('exibicao_dados.html', nome=nome, idade=idade, email=email)


if __name__ == '__main__':
    app.run(debug=True)
