// This is used to add more controll into Create/Update page.

/*
Requires core.js, SelectBox.js and SelectFilter2Custom.js 
*/

const FormChecker = {
    cache: '',
    selectBox: 0,
    init: function () {
        // falsy if no select Box in a Form and truthy if there is select Box in Form
        FormChecker.selectBox = window.SelectBox !== undefined ? Object.keys(window.SelectBox.cache).length : 0;
        FormChecker.tagsInput = document.querySelectorAll('input[data-role=tagsinput]').length !==0 ? true : false;
        // Cache the initial values of input fields.
        FormChecker.cache = FormChecker.getValuesString();
    },
    getValuesString: function () {
        // Get values from form (at current state) and make a string.
        let valuesString = '';
        getFormElements('input.textinput, textarea, select, input.urlinput, input[type=file]').forEach(elem => valuesString += elem.value);
        getFormElements('input.checkboxinput, input.radioinput').forEach(elem => valuesString += elem.checked);

        if (FormChecker.selectBox) {
            window.SelectBox.sortCache();
            let copiedSelectBoxCache = JSON.parse(JSON.stringify(window.SelectBox.cache));
            for (const key in copiedSelectBoxCache) {
                for (const i of copiedSelectBoxCache[key]) {
                    delete i['displayed'];
                }
              }
            valuesString += JSON.stringify(copiedSelectBoxCache);
        }
        if (FormChecker.tagsInput) {
            for (i of document.querySelectorAll('input[data-role=tagsinput]')) {
                for (tag of i.parentNode.querySelectorAll('.badge')) {
                    valuesString += tag.innerText;
                }
            }
        }
        return valuesString;
    },
    compare: function () {
        return FormChecker.cache === FormChecker.getValuesString();
    }
}

function getFormElements(selector) {
    const elements = [];
    document.querySelectorAll('#submit-btn').forEach(btn => elements.push(...btn.closest('form').querySelectorAll(selector)));
    return elements;
}

function toggleFormSubmit() {
    let btn = document.querySelector('#submit-btn');
    if (FormChecker.compare()) {
        btn.classList.add('disabled');
        btn.type = 'button';
    } else {
        btn.classList.remove('disabled');
        btn.type = 'submit';
    }
}

window.addEventListener('load', function (e) {
    FormChecker.init();

    getFormElements('input.textinput, textarea, input.urlinput')
        .forEach((elem) => {
            elem.addEventListener('change', toggleFormSubmit);
            if (elem.value) {
                if (elem.type == 'password') {
                    elem.parentNode.previousElementSibling.classList.remove('hidden-label');
                } else if(elem.type != 'textarea' && elem.previousElementSibling) {
                    elem.previousElementSibling.classList.remove('hidden-label');
                }
            }
        });

    getFormElements('input.checkboxinput, input.custom-textfield, input[type=file]')
        .forEach(elem => elem.addEventListener('change', toggleFormSubmit));

    getFormElements('input.radioinput, .dropdown-item')
        .forEach(elem => elem.addEventListener('click', toggleFormSubmit));

    if (FormChecker.selectBox) {
        document.querySelectorAll('.controls .selector select').forEach(function (el) {
            el.onclick = function () {
                el.querySelectorAll('option').forEach(function (op) {
                    if (op.selected) {
                        op.classList.add('option-selected');
                    } else {
                        op.classList.remove('option-selected');
                    }
                })
            }
        })

        document.querySelectorAll('.selector-chooseall, .selector-clearall, .selector-add, .selector-remove')
            .forEach(item => item.addEventListener('click', toggleFormSubmit));
    }
    if (FormChecker.tagsInput) {
        for (i of document.querySelectorAll('input[data-role=tagsinput]')) {
            $(i).on('itemAdded', toggleFormSubmit);
            $(i).on('itemRemoved', toggleFormSubmit);
        }
    }
})
