const togglePassword = $('#login-pass-toggle-icon');
const password = $('#login-password');
togglePassword.on('click', function (e) {
    // toggle the type attribute
    const type = password.attr('type') === 'password' ? 'text' : 'password';
    password.attr('type', type);
    let tClass = type === "text"? 'fas fa-eye inspecting-eye-icon': 'fas fa-eye';
    // toggle the eye slash icon
    togglePassword.removeClass().addClass(tClass);
});
//
// const inputs = document.querySelectorAll('.data-input');
// for (let i of inputs) {
//     i.addEventListener('focus', function() {
//         let label = document.querySelector(`.input-label[for="${i.getAttribute('id')}"]`);
//         label.classList.remove('hidden-label');
//     });
//     i.addEventListener('focusout', function() {
//         if (!i.value) {
//             let label = document.querySelector(`.input-label[for="${i.getAttribute('id')}"]`);
//             label.classList.add('hidden-label');
//         }
//     });
// }