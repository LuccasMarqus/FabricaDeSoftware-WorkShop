# Generated by Django 4.2.4 on 2023-09-02 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_cliente_endereco_alter_cliente_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='idade',
        ),
        migrations.AddField(
            model_name='cliente',
            name='Reclamacao',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='assunto',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=140, null=True),
        ),
    ]
