# Generated by Django 4.2.4 on 2023-08-31 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_rename_descricaoo_task_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='data',
            field=models.DateField(),
        ),
    ]
