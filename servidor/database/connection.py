import sqlite3

DATABASE = 'livros.db'


def conectar():

    return sqlite3.connect(DATABASE)


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