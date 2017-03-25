var toggle = function(el, className) {
    var buttons = document.getElementsByClassName("pure-button");
    for (j=0; j < buttons.length; j++){
        if (buttons[j] === el && !(buttons[j].classList.contains('pure-button-active'))) {
            el.classList.toggle('pure-button-active');
        } else if (buttons[j] !== el && buttons[j].classList.contains('pure-button-active')) {
            buttons[j].classList.toggle('pure-button-active');
        }

    };
    
    var nodes = document.getElementById('base').children;
    for(i=0; i < nodes.length; i++) {
        if (nodes[i].classList.contains(className)) {
            if (nodes[i].hasAttribute('hidden') === true) {
                nodes[i].removeAttribute('hidden');
            } 
        } else {
            if (nodes[i].hasAttribute('hidden') !== true) {
                nodes[i].setAttribute('hidden', '');            
        }
    }
}};
