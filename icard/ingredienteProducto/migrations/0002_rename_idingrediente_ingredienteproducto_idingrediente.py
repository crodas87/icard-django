# Generated by Django 4.1.7 on 2023-04-27 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingredienteProducto', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredienteproducto',
            old_name='IdIngrediente',
            new_name='idIngrediente',
        ),
    ]
