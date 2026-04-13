from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

ARQUIVO = 'imoveis.json'

if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, 'w') as f:
        json.dump([], f)

@app.route('/imoveis', methods=['GET'])
def get_imoveis():
    with open(ARQUIVO, 'r') as f:
        return jsonify(json.load(f))

@app.route('/imoveis', methods=['POST'])
def add_imovel():
    novo = request.json

    with open(ARQUIVO, 'r') as f:
        dados = json.load(f)

    dados.append(novo)

    with open(ARQUIVO, 'w') as f:
        json.dump(dados, f, indent=4)

    return jsonify({"msg": "Imóvel salvo!"})

if __name__ == "__main__":
    app.run()
