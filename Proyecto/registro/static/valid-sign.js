document.addEventListener('DOMContentLoaded', () => {
    // alert('Documento Listo')
});

const form = document.querySelector('form');

debugger
const nombre    = document.getElementById('inputNombre');
const apellido  = document.getElementById('inputApellido');
const email     = document.getElementById('inputEmail');
const password  = document.getElementById('pass');

form.addEventListener('submit', function (evt) {
    evt.preventDefault();
    
    const validEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

    if (nombre.value === null || nombre.value === '') {
        alert('Ingresa tu Nombre')
    }
    
    if (apellido.value === null || apellido.value === '') {
        alert('Ingresa tu Apellido')
    }

    if (email.value === null || email.value === '') {
        alert('Ingresa tu Correo')
    } else if (!validEmail.test(email.value)) {
        alert('Ingresa un Correo Valido')
    }

    if (password.value === null || password.value === '') {
        alert('Ingresa tu Contraseña')
    } else if (password.value.length < 8) {
        alert('La Contraseña debe tener al menos 8 caracteres')
    }
});

const pass = document.getElementById('pass');
const icon = document.querySelector('.bi');

icon.addEventListener('click', e => {
    if (pass.type === 'password') {
        pass.type = 'text';
        icon.classList.remove('bi-eye-slash')
        icon.classList.add('bi-eye')
    } else {
        pass.type = 'password'
        icon.classList.add('bi-eye-slash')
        icon.classList.remove('bi-eye')
    }
});