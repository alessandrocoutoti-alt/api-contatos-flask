from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


def conectar():
    conexao = sqlite3.connect("contatos.db")
    conexao.row_factory = sqlite3.Row
    return conexao
def criar_tabela():
    conexao = conectar()
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            email TEXT
        )
    """)
    conexao.commit()
    conexao.close()

criar_tabela()





@app.route("/contatos", methods=["GET"])
def listar_contatos():
    conexao = conectar()
    contatos = conexao.execute("SELECT * FROM contatos").fetchall()
    conexao.close()

    resultado = [dict(contato) for contato in contatos]
    return jsonify(resultado)

@app.route("/contatos", methods=["POST"])
def adicionar_contato():
    dados = request.get_json()

    nome = dados.get("nome")
    telefone = dados.get("telefone")
    email = dados.get("email")

    if not nome:
        return jsonify({"erro": "O campo 'nome' é obrigatório."}), 400

    conexao = conectar()
    conexao.execute(
        "INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)",
        (nome, telefone, email)
    )
    conexao.commit()
    conexao.close()

    return jsonify({"mensagem": f"Contato '{nome}' adicionado!"}), 201
@app.route("/contatos/<int:id_contato>", methods=["PUT"])
def atualizar_contato(id_contato):
    dados = request.get_json()

    nome = dados.get("nome")
    telefone = dados.get("telefone")
    email = dados.get("email")

    conexao = conectar()
    resultado = conexao.execute(
        "UPDATE contatos SET nome = ?, telefone = ?, email = ? WHERE id = ?",
        (nome, telefone, email, id_contato)
    )
    conexao.commit()
    conexao.close()

    if resultado.rowcount == 0:
        return jsonify({"erro": "Contato não encontrado."}), 404

    return jsonify({"mensagem": "Contato atualizado com sucesso!"})


@app.route("/contatos/<int:id_contato>", methods=["DELETE"])
def remover_contato(id_contato):
    conexao = conectar()
    resultado = conexao.execute("DELETE FROM contatos WHERE id = ?", (id_contato,))
    conexao.commit()
    conexao.close()

    if resultado.rowcount == 0:
        return jsonify({"erro": "Contato não encontrado."}), 404

    return jsonify({"mensagem": "Contato removido com sucesso!"})
    
@app.route("/")    
def home():
    return "API de Contatos no ar!"

if __name__ == "__main__":
    app.run(debug=True)