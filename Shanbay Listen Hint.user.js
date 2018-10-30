// ==UserScript==
// @name         Shanbay Listen Hint
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       Yang
// @match        https://www.shanbay.com/listen/sentence/
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    $(document).keydown(function(event){
	if(event.keyCode == 53){
        var textField = document.activeElement;
        textField.value = textField.getAttribute('data');
        return false;
	}
});
    // Your code here...
})();