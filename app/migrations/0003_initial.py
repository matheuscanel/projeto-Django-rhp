# Generated by Django 5.0.3 on 2024-03-07 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_delete_medicos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cracha', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11)),
                ('data_nascimento', models.CharField(max_length=12)),
                ('estado_nascimento', models.CharField(max_length=50)),
                ('cidade_nascimento', models.CharField(max_length=50)),
                ('sexo', models.CharField(max_length=50)),
                ('raca', models.CharField(max_length=50)),
                ('estado_civil', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=70)),
                ('celular', models.CharField(max_length=11)),
                ('cep', models.CharField(max_length=8)),
                ('estado', models.CharField(max_length=70)),
                ('cidade', models.CharField(max_length=70)),
                ('bairro', models.CharField(max_length=70)),
                ('endereco', models.CharField(max_length=70)),
                ('complemento', models.CharField(max_length=50)),
                ('grau_de_instrucao', models.CharField(max_length=50)),
                ('conselho', models.CharField(max_length=15)),
                ('especialidade', models.CharField(max_length=70)),
                ('especialidade2', models.CharField(max_length=70)),
                ('honorarios', models.CharField(max_length=70)),
                ('clinica1', models.CharField(max_length=70)),
                ('clinica2', models.CharField(max_length=70)),
                ('clinica3', models.CharField(max_length=70)),
            ],
        ),
    ]
