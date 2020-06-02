if (window.define) {
  define([
    'jquery',
    'pat-base',
  ], function($, Base) {
    'use strict';

  });
}

function setupPrivacyScreen() {
  var iframes = document.querySelectorAll('iframe');

  for (var i = 0; i < iframes.length; i++) {
    var node = iframes[i];
    var attr = node.getAttribute('data-embed-destination');
    var src = node.getAttribute('src');
    // TODO: use a definitive URL for @@embed
    // TODO: test for accepted cookie, use a setTimeout to check for it
    var url = './@@embed?src=' + encodeURI(src);
    if (attr) {
      node.setAttribute('src', url);
      console.log(node, attr, url);
    }
  }

}

window.onload = setupPrivacyScreen();
// window.addEventListener('DOMContentLoaded', setupPrivacyScreen);
