from flask import Flask, render_template, request, redirect, url_for, make_response
import json

app = Flask(__name__)

USUARIO_CADASTRADO = 'admin'
SENHA_CADASTRADA = '123'

@app.route('/', methods=['GET', 'POST'])
def login():
    mensagem = ""

    if request.method == "POST":

        usuario = request.form['username']
        senha = request.form['password']

        if usuario == USUARIO_CADASTRADO and senha == SENHA_CADASTRADA:
            resposta = make_response(redirect(url_for('bemvindo'))) #quando usamos o make_response, podemos atribuir os cookies, ter uma interação maior de css, html, jason. ele dá uma possibilidade maior. é um jeito mais detalhado de enviar informações para o navegador. com outras coisas, mandaríamos tudo junto embutido. já com o make_response, podemos passar informação aos poucos. 
            resposta.set_cookie('username', usuario, max_age=60*10) #linha que "seta" o cookie no seu navegador. a primeira informação é o nome da variável cookie, a segunda, que tipo de informação guarda, e a terceira, quanto tempo o navegador guardará seus cookies

            return resposta
        
        else:

            mensagem = "Usuário ou senha inválidos. Tente novamente."

    return render_template('login.html', error=mensagem)

@app.route('/bemvindo')
def bemvindo():
    username = request.cookies.get('username') #o request serve para ler os dados do cookie. get serve para ler e set, para pegar

    if not username:
        return redirect(url_for('login'))
    
    if request.method == "POST":
        cor_selecionada = request.form.get('cor')
        resp = make_response(render_template('bemvindo.html', cor_selecionada=cor_selecionada))
        resp.set_cookie("corSelecionada", cor_selecionada, path="/")
        return resp
   
    cor_cookie = request.cookies.get("corSelecionada")
    return render_template('bemvindo.html', cor_selecionada=cor_cookie)    

@app.route('/logout')
def logout():
    resposta = make_response(redirect(url_for('login')))

    resposta.set_cookie('username', '', expires=0) #esse expires=0 serve para "matar" essa variável do tipo cookie, tirá-lo do navegador

    return resposta

if __name__ == '__main__':
    app.run(debug = True)

#diferença entre sessão e cookie: a sessão, quando você sai do site, você perde aquelas informações. já o cookie, mesmo quando você sai, ela continua gravada.