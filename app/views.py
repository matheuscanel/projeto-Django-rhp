from django.shortcuts import render
from .models import Medicos
from .forms import formulario
from .automations.cod import automacao
import threading, time

# def chamar_automacao():
#     time.sleep(10)
#     automacao()

def cadastro(request):
    return render(request, 'cadastro.html')


def cadastro_concluido(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cracha = request.POST.get('cracha')
        cpf = request.POST.get('cpf')
        data_nascimento = request.POST.get('data_nascimento')
        estado_nascimento = request.POST.get('estado_nascimento')
        cidade_nascimento = request.POST.get('cidade_nascimento')
        sexo = request.POST.get('sexo')
        raca = request.POST.get('raca')
        estado_civil = request.POST.get('estado_civil')
        email = request.POST.get('email')
        celular = request.POST.get('celular')
        cep = request.POST.get('cep')
        estado = request.POST.get('estado')
        cidade = request.POST.get('cidade')
        bairro = request.POST.get('bairro')
        endereco = request.POST.get('endereco')
        complemento = request.POST.get('complemento')
        grau_de_instrucao = request.POST.get('grau_de_instrucao')
        conselho = request.POST.get('conselho')
        especialidade = request.POST.get('especialidade')
        especialidade2 = request.POST.get('especialidade2')
        honorarios = request.POST.get('honorarios')
        clinica1 = request.POST.get('clinica1')
        clinica2 = request.POST.get('clinica2')
        clinica3 = request.POST.get('clinica3')

        # Cria uma instância do modelo Medico com os dados do formulário
        medicos = Medicos(
            nome=nome,
            cracha=cracha,
            cpf=cpf,
            data_nascimento=data_nascimento,
            estado_nascimento=estado_nascimento,
            cidade_nascimento=cidade_nascimento,
            sexo=sexo,
            raca=raca,
            estado_civil=estado_civil,
            email=email,
            celular=celular,
            cep=cep,
            estado=estado,
            cidade=cidade,
            bairro=bairro,
            endereco=endereco,
            complemento=complemento,
            grau_de_instrucao=grau_de_instrucao,
            conselho=conselho,
            especialidade=especialidade,
            especialidade2=especialidade2,
            honorarios=honorarios,
            clinica1=clinica1,
            clinica2=clinica2,
            clinica3=clinica3
        )

        medicos.save()

        # threading.Thread(target=chamar_automacao).start()

    #add ao banco
    return render(request, "cadastro_concluido.html") 