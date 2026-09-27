import os
import sqlite3
from datetime import datetime
from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
from flasgger import Swagger
import yaml

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir chamadas da Interface/Front-end

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'database.db')
SQL_INIT_FILE = os.path.join(BASE_DIR, 'carga_inicial.sql')

# Conexão com o banco de dados SQLite
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Garante a criação e carga inicial do banco de dados se necessário
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='produtos'")
    if not cursor.fetchone():
        if os.path.exists(SQL_INIT_FILE):
            with open(SQL_INIT_FILE, 'r', encoding='utf-8') as f:
                conn.executescript(f.read())
            conn.commit()
    conn.close()

init_db()

# Configuração da documentação Swagger (OpenAPI 3.0) com Flasgger
swagger_path = os.path.join(BASE_DIR, 'swagger.yaml')
with open(swagger_path, 'r', encoding='utf-8') as f:
    swagger_template = yaml.safe_load(f)

# Define a versão do OpenAPI para evitar conflitos com o Swagger 2.0 padrão
app.config['SWAGGER'] = {
    'openapi': '3.0.0'
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec',
            "route": '/apispec.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger"
}

swagger = Swagger(app, config=swagger_config, template=swagger_template)


# Redireciona a página raiz para o Swagger UI
@app.route('/')
def index():
    return redirect('/swagger')


# ROTA 1: Listar todos os produtos (GET /api/produtos)
@app.route('/api/produtos', methods=['GET'])
def listar_produtos():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM produtos")
    linhas = cursor.fetchall()
    
    produtos = [dict(linha) for linha in linhas]
    conn.close()
    return jsonify(produtos), 200


# ROTA 2: Buscar produto por ID (GET /api/produtos/<id>)
@app.route('/api/produtos/<int:id>', methods=['GET'])
def obter_produto(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
    linha = cursor.fetchone()
    conn.close()
    
    if linha is None:
        return jsonify({"erro": "Produto não encontrado."}), 404
        
    return jsonify(dict(linha)), 200


# ROTA 3: Cadastrar um novo produto (POST /api/produtos)
@app.route('/api/produtos', methods=['POST'])
def cadastrar_produto():
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados inválidos ou corpo da requisição vazio."}), 400
        
    nome = dados.get('name')
    preco = dados.get('price')
    categoria = dados.get('category')
    descricao = dados.get('description', '')
    
    # Validações dos campos obrigatórios
    if not nome or preco is None or not categoria:
        return jsonify({"erro": "Campos 'name', 'price' e 'category' são obrigatórios."}), 400
        
    try:
        preco_float = float(preco)
        if preco_float < 0:
            return jsonify({"erro": "O preço do produto não pode ser negativo."}), 400
    except ValueError:
        return jsonify({"erro": "O preço deve ser um valor numérico válido."}), 400

    data_criacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO produtos (name, price, category, description, created_at) VALUES (?, ?, ?, ?, ?)",
        (nome, preco_float, categoria, descricao, data_criacao)
    )
    conn.commit()
    
    novo_id = cursor.lastrowid
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (novo_id,))
    novo_produto = cursor.fetchone()
    conn.close()
    
    return jsonify(dict(novo_produto)), 201


# ROTA 4: Atualizar um produto por ID (PUT /api/produtos/<id>)
@app.route('/api/produtos/<int:id>', methods=['PUT'])
def atualizar_produto(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
    produto_existente = cursor.fetchone()
    
    if produto_existente is None:
        conn.close()
        return jsonify({"erro": "Produto não encontrado para atualização."}), 404
        
    dados = request.get_json()
    if not dados:
        conn.close()
        return jsonify({"erro": "Dados inválidos."}), 400
        
    nome = dados.get('name')
    preco = dados.get('price')
    categoria = dados.get('category')
    descricao = dados.get('description', '')

    if not nome or preco is None or not categoria:
        conn.close()
        return jsonify({"erro": "Campos 'name', 'price' e 'category' são obrigatórios."}), 400
        
    try:
        preco_float = float(preco)
        if preco_float < 0:
            conn.close()
            return jsonify({"erro": "O preço do produto não pode ser negativo."}), 400
    except ValueError:
        conn.close()
        return jsonify({"erro": "O preço deve ser um valor numérico válido."}), 400

    cursor.execute(
        "UPDATE produtos SET name = ?, price = ?, category = ?, description = ? WHERE id = ?",
        (nome, preco_float, categoria, descricao, id)
    )
    conn.commit()
    
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
    produto_atualizado = cursor.fetchone()
    conn.close()
    
    return jsonify(dict(produto_atualizado)), 200


# ROTA 5: Deletar produto por ID (DELETE /api/produtos/<id>)
@app.route('/api/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
    produto = cursor.fetchone()
    
    if produto is None:
        conn.close()
        return jsonify({"erro": "Produto não encontrado para remoção."}), 404
        
    cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    
    return jsonify({"mensagem": "Produto removido com sucesso.", "id": id}), 200


# ROTA 6: Listar todas as categorias (GET /api/categorias)
@app.route('/api/categorias', methods=['GET'])
def listar_categorias():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM categorias")
    linhas = cursor.fetchall()
    
    categorias = [dict(linha) for linha in linhas]
    conn.close()
    return jsonify(categorias), 200


# ROTA 7: Buscar produtos por termo no nome (GET /api/produtos/busca)
@app.route('/api/produtos/busca', methods=['GET'])
def buscar_por_nome():
    termo = request.args.get('nome')
    if not termo:
        return jsonify({"erro": "Parâmetro de busca 'nome' é obrigatório."}), 400
        
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM produtos WHERE name LIKE ?", (f"%{termo}%",))
    linhas = cursor.fetchall()
    
    produtos = [dict(linha) for linha in linhas]
    conn.close()
    return jsonify(produtos), 200


# Executa o servidor Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
