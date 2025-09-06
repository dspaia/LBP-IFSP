document.addEventListener('DOMContentLoaded', () => {
    const botao = document.getElementById('carregar-btn');
    const divConteudo = document.getElementById('conteudo');

    botao.addEventListener('click', () => {
        divConteudo.innerHTML = '<p>Carregando livros...</p>';

        fetch('/api/livros')
            .then(res => res.json())
            .then(livros => {
                let html = '<div class="lista-livros">';
                livros.forEach(livro => {
                    html += `
                        <div class="livro">
                            <a href="${livro.link}">
                                <img src="${livro.imagem}" alt="${livro.titulo}">
                                <h3>${livro.titulo}</h3>
                                <p><strong>Autor:</strong> ${livro.autor}</p>
                                <p><strong>Avaliação:</strong> ${'⭐'.repeat(livro.avaliacao)} (${livro.avaliacao}/5)</p>
                                <p>${livro.descricao}</p>
                                <p><strong>Gênero:</strong> ${livro.genero}</p>
                                <p><strong>Páginas:</strong> ${livro.paginas}</p>
                            </a>
                        </div>
                    `;
                });
                html += '</div>';

                divConteudo.innerHTML = html;
            })
            .catch(err => {
                console.error(err);
                divConteudo.innerHTML = '<p>Erro ao carregar os livros.</p>';
            });
    });
});
