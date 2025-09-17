from flask import Flask, render_template, jsonify

app =Flask(__name__)
dados_biografias =  {
    "Santos Dumont":{
        "Nome": "Santos Dumont",
        "texto":"Alberto Santos de Dumont foi um aeronauta, esportista e inventor brasileiro"
    },
    
    "Marie Curie":{
        "Nome":"Marie Curie",
        "Texto":"Marie Sktodowska Curie foi uma física e quimica polonesa naturalizada francesa"
    },

    "Albert Einstein":{
        "Nome":"Albert Eisntein",
        "Texto":"Albert Einstein foi um físico teorico alemão que desenvolveu a teoria da relatividade"
    }

}


@app.route("/")
def index():
    personagens = dados_biografias.keys()

    return render_template("index.html", personagens=personagens, nomes=dados_biografias)


@app.route ("/biografia/<id_personagem>")
def get_biografia(id_personagem):

    biografia_data = dados_biografias.get(id_personagem,{
        "Nome":"Desconhecido",
        "Texto":"Personagem não encontrado"

    })

    return jsonify(biografia_data)


if __name__=="__main__":
    app.run(debug=True)