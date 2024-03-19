from django.db import models

class Medicos(models.Model):
    nome = models.CharField(max_length=150)
    cracha = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.CharField(max_length=12)
    estado_nascimento = models.CharField(max_length=50)
    cidade_nascimento = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    estado_civil = models.CharField(max_length=70)
    email = models.EmailField(max_length=70)
    celular = models.CharField(max_length=11)
    cep = models.CharField(max_length=8)
    estado = models.CharField(max_length=70)
    cidade = models.CharField(max_length=70)
    bairro = models.CharField(max_length=70)
    endereco = models.CharField(max_length=70)
    complemento = models.CharField(max_length=50)
    grau_de_instrucao = models.CharField(max_length=50)
    conselho = models.CharField(max_length=15)
    especialidade = models.CharField(max_length=70)
    especialidade2 = models.CharField(max_length=70)
    honorarios = models.CharField(max_length=70)
    clinica1 = models.CharField(max_length=70)
    clinica2 = models.CharField(max_length=70)
    clinica3 = models.CharField(max_length=70)

    def __str__(self):
        return self.nome
