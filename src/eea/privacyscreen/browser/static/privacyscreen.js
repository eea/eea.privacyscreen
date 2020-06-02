// Generic script to be embedded on any Plone site
// It discovers all <iframes> and replaces their destination to the /@@embed
// location

function setupPrivacyScreen() {
  var iframes = document.querySelectorAll('iframe');

  for (var i = 0; i < iframes.length; i++) {
    var node = iframes[i];
    var group = node.getAttribute('data-embed-group');
    var screenshot = node.getAttribute('data-embed-screenshot');
    var src = node.getAttribute('src');
    // TODO: use a definitive URL for @@embed
    // TODO: test for accepted cookie, use a setTimeout to check for it

    var url = './@@embed?group=' + group +
      '&screenshot=' + screenshot +
      '&src=' + encodeURI(src);

    if (group) {
      node.setAttribute('src', url);
      console.log(node, group, url);
    }
  }

}

window.onload = setupPrivacyScreen();

if (window.define) {
  define([
    'jquery',
    'pat-base',
  ], function($, Base) {
    'use strict';

  });
}

