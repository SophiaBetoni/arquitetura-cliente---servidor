const API = '/livros';

async function carregarLivros() {

    const resposta = await fetch(API);

    const livros = await resposta.json();

    mostrarLivros(livros);
}


function mostrarLivros(livros) {

    const lista = document.getElementById('lista-livros');

    lista.innerHTML = '';

    livros.forEach(livro => {

        lista.innerHTML += `
            <div class="livro">

                <div class="info-livro">

                    <strong>${livro.titulo}</strong><br>

                    <small>${livro.autor}</small><br><br>

                    <span>
                        ${livro.reservado ? '📕 Reservado' : '📗 Disponível'}
                    </span>

                </div>

                <div class="botoes">

                    <button
                        class="reservado"
                        onclick="reservarLivro(${livro.id})"
                    >
                        Reservar
                    </button>

                    <button
                        class="remover"
                        onclick="removerLivro(${livro.id})"
                    >
                        Remover
                    </button>

                </div>

            </div>
        `;
    });
}


async function salvarLivro() {

    const titulo = document.getElementById('titulo').value;

    const autor = document.getElementById('autor').value;

    if (!titulo || !autor) {

        alert('Preencha todos os campos');

        return;
    }

    try {

        const resposta = await fetch(API, {

            method: 'POST',

            headers: {
                'Content-Type': 'application/json'
            },

            body: JSON.stringify({
                titulo: titulo,
                autor: autor
            })
        });

        console.log(await resposta.json());

        document.getElementById('titulo').value = '';
        document.getElementById('autor').value = '';

        carregarLivros();

    } catch (erro) {

        console.error(erro);

        alert('Erro ao adicionar livro');
    }
}


async function reservarLivro(id) {

    await fetch(`${API}/reservar/${id}`, {

        method: 'PUT'
    });

    carregarLivros();
}


async function removerLivro(id) {

    await fetch(`${API}/${id}`, {

        method: 'DELETE'
    });

    carregarLivros();
}


carregarLivros();