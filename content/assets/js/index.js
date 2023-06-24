$(document).on('click', '.delete-confirmation', function(){
    return confirm('Are you sure you want to delete this?');
})

window.addEventListener('load', function(e){
    const inputs = document.querySelectorAll('.data-input');
    for (let i of inputs) {
        i.addEventListener('focus', function() {
            let label = document.querySelector(`.input-label[for="${i.getAttribute('id')}"]`);
            label.classList.remove('hidden-label');
        });
        i.addEventListener('focusout', function() {
            if (!i.value) {
                let label = document.querySelector(`.input-label[for="${i.getAttribute('id')}"]`);
                label.classList.add('hidden-label');
            }
        });
    }

    // Show label if fields have data, TODO: refactor code
    document.querySelectorAll('input.textinput, input.data-input')
    .forEach((elem) => {
        if (elem.value) {
            if (elem.type == 'password') {
                elem.parentNode.previousElementSibling.classList.remove('hidden-label');
            } else if(elem.type != 'textarea' && elem.previousElementSibling) {
                elem.previousElementSibling.classList.remove('hidden-label');
            }
        }
    });
})
