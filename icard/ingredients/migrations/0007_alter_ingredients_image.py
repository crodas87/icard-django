# Generated by Django 4.1.7 on 2023-04-21 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0006_alter_ingredients_image_alter_ingredients_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='image',
            field=models.ImageField(null=True, upload_to='products'),
        ),
    ]
