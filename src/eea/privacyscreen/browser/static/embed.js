// some code from https://gist.github.com/litodam/3048775
function CookiesHelper() {}

// usage
// CookiesHelper.createCookie("myCookieUniqueName", value, 30);
// CookiesHelper.createCookie("myJsonCookieUniqueName", json, 30);
CookiesHelper.createCookie = function(name, domain, days) {
  if (days) {
    var date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    var expires = "; expires=" + date.toGMTString();
  }

  if (domain) {
    domain = "; domain=" + domain;
  }

  else expires = "";
  var cookie = name + "=true" + domain + expires + "; path=/";
  console.log('cookie', cookie);
  document.cookie = cookie;
}

// usage
// var value = CookiesHelper.readCookie("myCookieUniqueName");
// var json = JSON.parse(CookiesHelper.readCookie("myJsonCookieUniqueName");
CookiesHelper.readCookie = function(name) {
  var nameEQ = name + "=";
  var ca = document.cookie.split(';');
  for (var i = 0; i < ca.length; i++) {
    var c = ca[i];
    while (c.charAt(0) == ' ') c = c.substring(1, c.length);
    if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
  }
  return null;
}

CookiesHelper.eraseCookie = function(name) {
  CookiesHelper.createCookie(name, "", -1);
}

function onSubmit(event) {
  console.log(event);
  event.preventDefault();
  var form = event.target;
  var remember = form.remember.checked;
  var applyAll = form.apply_to_all.checked;
  var domain = form.cookie_domain.value;
  var days = form.lifetime_days.value;
  var cookie_name = form.group.value;
  var iframe_url = form.iframe_url.value;
  CookiesHelper.createCookie(cookie_name, domain, days);
  document.location = iframe_url;
}

function setupEmbed () {
  var forms = document.querySelectorAll('form');
  var form = forms[0];
  form.addEventListener('submit', onSubmit);
}

window.onload = setupEmbed;
