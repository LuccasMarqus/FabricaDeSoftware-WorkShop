# Generated by Django 4.2.4 on 2023-08-31 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='date',
            new_name='data',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='descrição',
            new_name='descricaoo',
        ),
    ]
