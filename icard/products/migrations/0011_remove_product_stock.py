# Generated by Django 4.1.7 on 2023-07-05 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_alter_product_options_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]
