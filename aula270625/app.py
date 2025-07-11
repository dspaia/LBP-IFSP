from flask import Flask, render_template, url_for, session, redirect, request
import time

app = Flask(__name__)

app.secret_key = "chave-secreta"

usuarios = [
    {'username': 'joao123', 'password': '123'},
    {'username': 'maria456', 'password': '456'},
    {'username': 'jose789', 'password': '789'}
]

@app.route('/')

def home():

    return render_template('login.html')


@app.route('/lista')

def lista():
    produtos = ['Maçã', 'Banana', 'Laranja']
    logado = 'username' in session
    return render_template('home.html', produtos=produtos, logado=logado)

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for usuario in usuarios:
            if usuario['username'] == username and usuario['password'] == password:
                session ['username'] = username
                return render_template('profile.html', username=username)
            
        return 'Usuário ou senha inválidos'
    
    return render_template('login.html')

@app.route('/profile')

def perfil_logado():
    if 'username' in session:
        return f"<h1>Bem vindo de volta, {session['username']}!</h1>"
    return redirect(url_for('login'))

@app.route('/logout')

def logout():
    session.pop('username', None)
    return "Você foi deslogado"

@app.route('/redirecionar')
def redirecionar():
    time.sleep(2)
    return redirect(url_for('login.html'))

@app.route('/user/<username>')
def perfil_publico (username):
    return render_template('profile.html', user=username)

if __name__ == '__main__':
    app.run(debug=True)

#http://127.0.0.1:5000/user/<username>
