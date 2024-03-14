

$(document).ready(function () {
    // Aplicar a máscara ao campo de CPF
    $('input[name="cpf"]').inputmask('999.999.999-99', { placeholder: '000.000.000-00' });

    // Aplicar a máscara ao campo de CEP
    $('input[name="cep"]').inputmask('99999-999', { placeholder: '_____-___' });

    // Aplicar a máscara ao campo de Data de Nascimento
    $('input[name="data_nascimento"]').inputmask('99/99/9999', { placeholder: '__/__/____' });

    // Aplicar a máscara ao campo de Celular
    $('input[name="celular"]').inputmask('(99) 99999-9999', { placeholder: '(__) _____-____' });


});


function allStaties() {
    const estados = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal',
        'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais',
        'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte',
        'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins'];

    //para cada novo input com id, eu devo chamar no getElementById    
    const selectEstados1 = document.getElementById('estado_nascimento');
    const selectEstados2 = document.getElementById('estado');

    estados.forEach(function (estado) {
        const option1 = document.createElement('option'); // Cria um novo elemento <option>
        const option2 = document.createElement('option');
        option1.value = estado; // Define o valor da opção como o nome do estado
        option1.textContent = estado; // Define o texto da opção como o nome do estado
        option2.value = estado; // Define o valor da opção como o nome do estado
        option2.textContent = estado; // Define o texto da opção como o nome do estado
        selectEstados1.appendChild(option1); // Adiciona a opção ao combobox
        selectEstados2.appendChild(option2);
    });

}

window.onload = allStaties;


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

