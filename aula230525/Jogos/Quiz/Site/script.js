const readyModal = document.getElementById('ready-modal');
const mainContent = document.getElementById('main-content');
const startBtn = document.getElementById('start-btn');
const notNowBtn = document.getElementById('not-now-btn');
const modalElement = readyModal.querySelector('.modal');

function trapFocus(element) {
  const focusable = element.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
  if (!focusable.length) return;
  const firstFocusable = focusable[0];
  const lastFocusable = focusable[focusable.length - 1];
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
    if (e.key === 'Escape') {
      e.preventDefault(); 
    }
  });
}

trapFocus(modalElement);

mainContent.classList.add('blurred');
startBtn.focus();

startBtn.addEventListener('click', () => {
  readyModal.style.display = 'none';
  mainContent.classList.remove('blurred');
  mainContent.focus();
});

notNowBtn.addEventListener('click', () => {
  startBtn.focus();
});
