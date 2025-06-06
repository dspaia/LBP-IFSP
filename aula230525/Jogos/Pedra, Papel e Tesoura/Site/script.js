(function(){
  const modal = document.getElementById('match-modal');
  const singleBtn = document.getElementById('single-match');
  const numMatchesInput = document.getElementById('num-matches');
  const startBtn = document.getElementById('start-button');
  const resultScreen = document.getElementById('result-screen');

  let selectedMode = null; 

  function trapFocus(element) {
    const focusable = element.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
    const firstFocusable = focusable[0];
    const lastFocusable = focusable[focusable.length -1];
    element.addEventListener('keydown', (e) => {
      if (e.key === 'Tab') {
        if (e.shiftKey) {
          if (document.activeElement === firstFocusable) {
            e.preventDefault();
            lastFocusable.focus();
          }
        } else {
          if (document.activeElement === lastFocusable) {
            e.preventDefault();
            firstFocusable.focus();
          }
        }
      }
      if(e.key === 'Escape') {
        e.preventDefault();
      }
    });
  }
  trapFocus(modal);

  singleBtn.addEventListener('click', () => {
    selectedMode = 'single';
    numMatchesInput.value = '';
    startBtn.disabled = false;
    singleBtn.style.borderColor = 'var(--color-secondary)';
    singleBtn.style.backgroundColor = 'var(--color-secondary)';
    numMatchesInput.style.borderColor = 'var(--color-border)';
  });

  numMatchesInput.addEventListener('input', () => {
    if(numMatchesInput.value && Number(numMatchesInput.value) >=1){
      selectedMode = Number(numMatchesInput.value);
      startBtn.disabled = false;
      singleBtn.style.borderColor = 'var(--color-border)';
      singleBtn.style.backgroundColor = 'transparent';
    } else {
      startBtn.disabled = true;
      selectedMode = null;
    }
  });

  startBtn.addEventListener('click', () => {
    if(selectedMode !== null){
      modal.style.display = 'none';
      resultScreen.textContent = 'O jogo começará em breve. (Aqui será mostrado o vencedor.)';
      resultScreen.style.display = 'block';
    }
  });

  singleBtn.focus();
})();
