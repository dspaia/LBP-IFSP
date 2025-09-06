const botao = document.getElementById('carregar-btn');
const divConteudo = document.getElementById('conteudo');

botao.addEventListener('click', () => {
    fetch('/api/livros')
    .then(response => response.json())
    .then(livros => {
        let html = '';
        livros.forEach(livro => {
            html += livro.conteudo;
        });
        divConteudo.innerHTML = html;
    })
    .catch(err => {
        divConteudo.innerHTML = '<p>Erro ao carregar os livros.</p>';
        console.error(err);
    });
});
