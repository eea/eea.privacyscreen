// Javascript handlers for the replaced embedded content.
// This runs in the replacement iframe, and is served by @@embed
//
// some code from https://gist.github.com/litodam/3048775
function CookiesHelper() {}

CookiesHelper.createCookie = function(name, domain, days) {
  var expires = '';
  if (days) {
    var date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    expires = ';' + 'expires=' + date.toGMTString(); };

  domain = false;
  if (domain) {
    if (document.location.host.indexOf(domain) === -1) {
      domain = document.location.host;
    }
    domain = ';domain=' + domain;
  } else domain = '';

  var cookie = name + '=true' + domain + expires + ';path=/';
  document.cookie = cookie;
};

CookiesHelper.eraseCookie = function(name) {
  CookiesHelper.createCookie(name, '', -1);
};

function onSubmit(event) {
  event.preventDefault();
  var form = event.target;
  var remember = form.remember.checked;

  // var applyAll = form.apply_to_all.checked;
  if (remember) {
    var domain = form.cookie_domain.value;
    var days = form.lifetime_days.value;
    var cookie_name = 'embed_' + form.group.value;
    CookiesHelper.createCookie(cookie_name, domain, days);
  }

  var iframe_url = form.iframe_url.value;
  document.location = iframe_url;
}

function setupEmbed () {
  var forms = document.querySelectorAll('form');
  var form = forms[0];
  form.addEventListener('submit', onSubmit);
}

window.onload = setupEmbed;
