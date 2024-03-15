

$(document).ready(function () {
    // Aplicar a máscara ao campo de CPF
    $('input[name="cpf"]').inputmask('999.999.999-99', { placeholder: '000.000.000-00' });

    // Aplicar a máscara ao campo de CEP
    $('input[name="cep"]').inputmask('99999-999', { placeholder: '_____-___' });

    // Aplicar a máscara ao campo de Data de Nascimento
     
    $('input[name="data_nascimento"]').inputmask('99/99/9999', { placeholder: '__/__/____' });

    // Aplicar a máscara ao campo de Celular
    $('input[name="celular"]').inputmask('(99) 99999-9999', { placeholder: '(__) _____-____' });

    $('.select2').select2({
        placeholder: 'Selecione o estado',
        allowClear: true
      });
});

function validateForm() {
    var form = document.getElementById('cadastroForm');
    var elements = form.elements;

    for (var i = 0; i < elements.length; i++) {
        if (elements[i].required && elements[i].value.trim() === '') {
            alert('Por favor, preencha todos os campos obrigatórios.');
            return false;
        }

        if (elements[i].name === 'email' && !isValidEmail(elements[i].value)) {
            alert('Por favor, insira um endereço de email válido.');
            return false;
        }
    }

    return true;
}

function isValidEmail(email) {
    // Expressão regular simples para validação de email
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

