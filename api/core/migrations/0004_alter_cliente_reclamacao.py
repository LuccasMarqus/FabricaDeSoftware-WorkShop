# Generated by Django 4.2.4 on 2023-09-02 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_cliente_endereco_remove_cliente_idade_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='Reclamacao',
            field=models.TextField(),
        ),
    ]