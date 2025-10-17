from flask import Flask, render_template, request, abort, jsonify
import math

app =  Flask(__name__)

# NOSSA "BASE DE DADOS" EM MEMÓRIA

# Uma lista de dicionários

PRODUTOS = [
    {"id": 1, "nome": "Notebook Gamer X", "preco": 5200.00},
    {"id": 2, "nome": "Mouse sem fio", "preco": 150.00},
    {"id": 3, "nome": "Teclado mecânico RGB", "preco": 350.00},
    {"id": 4, "nome": "Monitor 27 polegadas", "preco": 1800.00},
    {"id": 5, "nome": "Headset rosa", "preco": 1500.00},
    {"id": 6, "nome": "Memória RAM 16GB", "preco": 500.00},
    {"id": 7, "nome": "Placa de vídeo mais foda que tem", "preco": 10000.00},
    {"id": 8, "nome": "Processador i900", "preco": 9000.00},
    {"id": 9, "nome": "PC Gamer completo transparente", "preco": 25000.00},
    {"id": 10, "nome": "Cadeira gamer ultra mega blaster confortável", "preco": 4000.00}
]

@app.route('/produtos')
def listar_produtos():
    return render_template('produtos.html', produtos = PRODUTOS)

@app.route('/produtos-paginados')
def listar_produtos_paginados():
    page = request.args.get('page', 1, type=int)
    per_page = 5 # itens por página

    # lógica da paginação
    start = (page - 1) * per_page
    end = start + per_page
    total_pages = math.ceil(len(PRODUTOS)/per_page)

    # fatiando a lista para pegar apenas os itens da página atual
    produtos_da_pagina = PRODUTOS[start:end]

    return render_template('produtos_paginados.html', produtos=produtos_da_pagina, page=page, total_pages=total_pages)

@app.route('/produto/<int:produto_id>')
def detalhe_produto(produto_id):
    produto_encontrado = None

    # busca pelo produto na lista (performance 0 (n))

    for produto in PRODUTOS:
        if produto["id"] == produto_id:
            produto_encontrado = produto
            break
    if produto_encontrado is None:
        abort(404) # item não encontrado

    return render_template('detalhe_produto.html', produto=produto_encontrado)

@app.route('/api/buscar-produto', methods=['POST'])
def buscar_produto():
    dados = request.get_json()
    nome_produto = dados.get('nome').lower()

    #busca na nossa lista de dicionários
    resultado = [p for p in PRODUTOS if nome_produto in p['nome'].lower()]

    return jsonify({'produtos_encontrados': resultado})

if __name__ == '__main__':
    app.run(debug=True)