// Generic script to be embedded on any Plone site
// It discovers all <iframes> and replaces their destination to the /@@embed
// location.
// Ideally we would also have a version of this script that runs as a
// - portal transform (for safe_html)
// - diazo transform (for stuff that's not richtext)

function CookiesHelper() {}

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

function setupPrivacyScreen() {
  var iframes = document.querySelectorAll('iframe');

  for (var i = 0; i < iframes.length; i++) {
    var node = iframes[i];
    var group = node.getAttribute('data-embed-group');
    var screenshot = node.getAttribute('data-embed-screenshot');
    screenshot = screenshot ? '&screenshot=' + encodeURI(screenshot) : '';
    var src = node.getAttribute('src');
    // TODO: use a definitive URL for @@embed
    // TODO: test for accepted cookie, use a setTimeout to check for it

    var url = './@@embed?group=' + group + screenshot +
      '&src=' + encodeURI(src);

    if (group) {
      if (!CookiesHelper.readCookie('embed_' + group)) {
        node.setAttribute('src', url);
      }
    }
  }

}

window.onload = setupPrivacyScreen();

// if (window.define) {
//   define([
//     'jquery',
//     'pat-base',
//   ], function($, Base) {
//     'use strict';
//
//   });
// }
//
