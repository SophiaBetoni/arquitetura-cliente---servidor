from flask import Blueprint, request, jsonify

from services.livros_service import (
    listar_livros,
    salvar_livro,
    reservar_livro,
    remover_livro
)

livros_routes = Blueprint('livros_routes', __name__)


@livros_routes.route('/livros', methods=['GET'])
def get_livros():

    return jsonify(listar_livros())


@livros_routes.route('/livros', methods=['POST'])
def post_livro():

    dados = request.json

    salvar_livro(
        dados['titulo'],
        dados['autor']
    )

    return jsonify({
        'mensagem': 'Livro salvo'
    })


@livros_routes.route('/livros/reservar/<int:id>', methods=['PUT'])
def put_reserva(id):

    reservar_livro(id)

    return jsonify({
        'mensagem': 'Livro reservado'
    })


@livros_routes.route('/livros/<int:id>', methods=['DELETE'])
def delete_livro(id):

    remover_livro(id)

    return jsonify({
        'mensagem': 'Livro removido'
    })