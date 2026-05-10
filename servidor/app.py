from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)

CORS(app)


def conectar():

    return sqlite3.connect('livros.db')


def criar_tabela():

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            titulo TEXT NOT NULL,

            autor TEXT NOT NULL,

            reservado INTEGER DEFAULT 0
        )
    ''')

    conn.commit()

    conn.close()


criar_tabela()


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/livros', methods=['GET'])
def listar_livros():

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute('SELECT * FROM livros')

    livros = cursor.fetchall()

    conn.close()

    resultado = []

    for livro in livros:

        resultado.append({

            'id': livro[0],

            'titulo': livro[1],

            'autor': livro[2],

            'reservado': bool(livro[3])
        })

    return jsonify(resultado)


@app.route('/livros', methods=['POST'])
def salvar_livro():

    dados = request.json

    titulo = dados['titulo']

    autor = dados['autor']

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute(
        '''
        INSERT INTO livros
        (titulo, autor)

        VALUES (?, ?)
        ''',
        (titulo, autor)
    )

    conn.commit()

    conn.close()

    return jsonify({
        'mensagem': 'Livro salvo'
    })


@app.route('/livros/reservar/<int:id>', methods=['PUT'])
def reservar_livro(id):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute(
        '''
        UPDATE livros
        SET reservado = 1
        WHERE id = ?
        ''',
        (id,)
    )

    conn.commit()

    conn.close()

    return jsonify({
        'mensagem': 'Livro reservado'
    })


@app.route('/livros/<int:id>', methods=['DELETE'])
def remover_livro(id):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute(
        'DELETE FROM livros WHERE id = ?',
        (id,)
    )

    conn.commit()

    conn.close()

    return jsonify({
        'mensagem': 'Livro removido'
    })


if __name__ == '__main__':

    app.run(debug=True)
