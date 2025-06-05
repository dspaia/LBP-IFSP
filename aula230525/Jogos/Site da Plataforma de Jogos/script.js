(function(){
  // elementos principais do carrossel
  const pistaCarrossel = document.querySelector('.pista-carrossel');
  const itensCarrossel = Array.from(pistaCarrossel.children);
  const botaoAnterior = document.querySelector('.botao-anterior');
  const botaoProximo = document.querySelector('.botao-proximo');
  let indiceAtual = 0;

  // função para obter a largura de um item
  function larguraItem() {
    return itensCarrossel[0].getBoundingClientRect().width;
  }

  // atualiza a posição do carrossel e os estados dos botões
  function atualizarCarrossel() {
    const distancia = -larguraItem() * indiceAtual;
    pistaCarrossel.style.transform = 'translateX(' + distancia + 'px)';
    atualizarBotoes();
  }

  // atualiza o estado (habilitado/desabilitado) dos botões
  function atualizarBotoes() {
    botaoAnterior.disabled = (indiceAtual === 0);
    botaoProximo.disabled = (indiceAtual === itensCarrossel.length - 1);
  }

  // evento clique no botão anterior
  botaoAnterior.addEventListener('click', () => {
    if (indiceAtual > 0) {
      indiceAtual--;
      atualizarCarrossel();
    }
  });

  // evento clique no botão próximo
  botaoProximo.addEventListener('click', () => {
    if (indiceAtual < itensCarrossel.length - 1) {
      indiceAtual++;
      atualizarCarrossel();
    }
  });

  // atualiza o carrossel no redimensionamento da janela
  window.addEventListener('resize', () => {
    atualizarCarrossel();
  });

  // inicializa o carrossel
  atualizarCarrossel();
})();
