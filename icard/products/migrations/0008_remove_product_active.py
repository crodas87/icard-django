# Generated by Django 4.1.7 on 2023-04-27 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_ingredientes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='active',
        ),
    ]
