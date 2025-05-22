from flask import render_template, Flask

app = Flask(__name__)

@app.route('/bemvindo/<nome>')
def bemvindo(nome):
    return render_template('index.html', usuario=nome)

@app.route('/')
def olamundo():
    return 'Olá Mundo!'

if __name__ == "__main__":
    app.run(debug=True)
