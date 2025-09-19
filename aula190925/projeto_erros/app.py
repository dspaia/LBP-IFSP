from flask import Flask, render_template, abort, request, flash, redirect, url_for  

app = Flask(__name__)

app.config['SECRET-KEY'] = 'uma-chave-secreta-muito-segura'

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # em uma aplicacao real, aqui ocorreria a validacao no back-end

        nome = request.form.get('nome')
        email = request.form.get('email')

        print(f"Dados recibidos do formulário: Nome = {nome}, Email = {email}")
        
        # simula mensagem de sucesso

        flash (f"Obrigado por se cadastrar, {nome}!", "sucess")

        return render_template(url_for('formulario.html'))

    return render_template('formulario.html')

@app.route('/')
def index():
    return render_template('index.html')

# para demonstrar o erro 401, vamos criar uma rota que exige um login (simulado)

@app.route('/area-restrita')
def area_restrita():
    # em uma aplicação real, aqui você verificaria se o usuário está logado
    # como não temos um sistema de login, vamos forçar o erro 401 com o abort()

    print('Tentativa de acesso à area restrita sem autenticação.')
    abort(401)

# para demonstrar o erro 403, uma rota de admin (simulado)

@app.route('/painel-admin')
def painel_admin():
    # aqui, verificaria se o usuário logado é um administrador
    # vamos simular que o usuário não é admin e forçar o erro 403

    print('Tentativa de acesso ao painel de admin sem permissão')
    abort(403)

# manipuladores de erro (Error Handlers)

@app.errorhandler(404)
def pagina_nao_encontrada(error):
    # a funcao recebe o objeto de erro como argumento.
    # retornamos a renderizacao do nosso template e o codigo de status 404

    return render_template('404.html'), 404

@app.errorhandler(401)
def nao_autorizado(error):

    return render_template('401.html'), 401

@app.errorhandler(403)
def acesso_proibido(error):

    return render_template('403.html'), 403

if __name__ == '__main__':
    app.run(debug=True)





