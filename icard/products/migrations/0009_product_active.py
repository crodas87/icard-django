# Generated by Django 4.1.7 on 2023-04-27 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_product_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
