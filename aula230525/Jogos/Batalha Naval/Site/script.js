document.addEventListener("DOMContentLoaded", () => {
  const tabuleiroJogador = document.querySelector("#tabuleiro-jogador .grid");
  const tabuleiroComputador = document.querySelector("#tabuleiro-computador .grid");
  const linhaInput = document.getElementById("linha");
  const colunaInput = document.getElementById("coluna");
  const mensagemEl = document.getElementById("mensagem");
  const btnAtacar = document.querySelector(".btn-attack");

  function inicializarTabuleiro(grid) {
    grid.innerHTML = "";
    for (let i = 0; i < 100; i++) {
      const cell = document.createElement("div");
      cell.classList.add("cell");
      cell.setAttribute("role", "gridcell");
      cell.setAttribute("aria-label", `Célula ${Math.floor(i / 10)}, ${i % 10}`);
      grid.appendChild(cell);
    }
  }
  inicializarTabuleiro(tabuleiroJogador);
  inicializarTabuleiro(tabuleiroComputador);

  linhaInput.disabled = true;
  colunaInput.disabled = true;
  btnAtacar.disabled = true;

  function atualizarMensagem(texto) {
    mensagemEl.textContent = texto;
  }

  document.querySelector(".form-attack").addEventListener("submit", (event) => {
    event.preventDefault();
    atualizarMensagem("Funcionalidade de ataque será implementada em breve.");
  });
});
