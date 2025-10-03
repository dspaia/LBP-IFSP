from flask import Flask, render_template, request, redirect, url_for, session, make_response
from models import UsuarioModel # Importa nosso modelo

app = Flask(__name__)
usuario_model = UsuarioModel() # Instancia o modelo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuarios')
def listar_usuarios():
    """
    1. Controle pede os dados ao modelo.
    2. Modelo retorna a lista de usuários.
    3. Controle entrega a lista para a visão renderizar.
    """

    usuarios = usuario_model.get_todos()

    return render_template('usuarios.html', lista_de_usuarios=usuarios)

@app.route('/usuarios/novo', methods=['POST'])
def adicionar_usuario():
    """
    1. Controle recebe os dados do formulário (enviados pela Visão).
    2. Controle pede para o Modelo salvar os novos dados.
    3. Controle redireciona o usuário para a página inicial.
    """

    nome = request.form['nome']
    email = request.form['email']

    usuario_model.salvar(nome, email)

    return redirect(url_for('listar_usuarios'))

if __name__=='__main__':
    app.run(debug=True)