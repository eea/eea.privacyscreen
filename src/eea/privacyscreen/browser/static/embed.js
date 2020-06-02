function onSubmit() {
  event.preventDefault();
  document.location = iframe_url;
}

function setupEmbed () {
  var forms = document.querySelectorAll('form');
  var form = forms[0];
  form.addEventListener('submit', onSubmit);
}

window.onload = setupEmbed;
