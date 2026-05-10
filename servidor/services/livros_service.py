from database.connection import conectar


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

    return resultado


def salvar_livro(titulo, autor):

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


def remover_livro(id):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute(
        'DELETE FROM livros WHERE id = ?',
        (id,)
    )

    conn.commit()

    conn.close()