# Generated by Django 4.1.7 on 2023-07-02 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0009_remove_ingredients_quantity_ingredients_um'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='image',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]