let toggleConfirm = $('#confirm-pass-toggle-icon');
const confirmPassword = $('#confirm-password');
toggleConfirm.on('click', function (e) {
    // toggle the type attribute
    const type = confirmPassword.attr('type') === 'password' ? 'text' : 'password';
    confirmPassword.attr('type', type);
    let tClass = type === "text"? 'fas fa-eye inspecting-eye-icon': 'fas fa-eye';
    // toggle the eye slash icon
    toggleConfirm.removeClass().addClass(tClass);
});