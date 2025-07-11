document.getElementById('corFormulario').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    const corSelecionada = document.getElementById('cor').value;
    document.body.style.backgroundColor = corSelecionada;

    document.cookie = "corSelecionada=" + corSelecionada + ";path=/";
  });

  // Carregar a cor do cookie ao carregar a página
  document.addEventListener('DOMContentLoaded', function() {
    const valorCookie = document.cookie.split('; ')
      .find(row => row.startsWith('corSelecionada='))
      ?.split('=')[1];

    if (valorCookie) {
      document.body.style.backgroundColor = valorCookie;
    }
  });