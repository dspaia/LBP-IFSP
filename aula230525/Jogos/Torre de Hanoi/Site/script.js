// script.js
// Currently, no game logic. UI is static and ready for future integration.

// Accessibility: Announce status message changes smoothly.
const mensagemEl = document.getElementById('mensagem');

// Placeholder function for future move events
function handleMove() {
  mensagemEl.textContent = 'Função de mover disco será implementada em breve.';
}

// Attach event listener for future form submission
document.querySelector('.form-move').addEventListener('submit', e => {
  e.preventDefault();
  handleMove();
});

// Focus management: add subtle focus trap to main interactive region when enabled.
// Currently no enabled controls, so minimal behavior for future proofing.
document.addEventListener('DOMContentLoaded', () => {
  // For now, nothing interactive to implement.
});
