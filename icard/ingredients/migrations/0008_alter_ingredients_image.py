# Generated by Django 4.1.7 on 2023-04-21 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0007_alter_ingredients_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='products'),
        ),
    ]
