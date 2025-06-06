const input = document.getElementById('guess-input');
const button = document.querySelector('.btn-submit');

input.addEventListener('input', () => {
  const val = input.value;
  if (val !== '' && !isNaN(val) && Number(val) >= 0 && Number(val) <= 100) {
    button.disabled = false;
  } else {
    button.disabled = true;
  }
});
