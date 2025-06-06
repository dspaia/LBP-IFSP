const mensagemEl = document.getElementById('mensagem');

function handleMove() {
  mensagemEl.textContent = 'Função de mover disco será implementada em breve.';
}

document.querySelector('.form-move').addEventListener('submit', e => {
  e.preventDefault();
  handleMove();
});

document.addEventListener('DOMContentLoaded', () => {
});
