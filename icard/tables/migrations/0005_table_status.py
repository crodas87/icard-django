# Generated by Django 4.1.7 on 2023-03-06 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0004_table_codorder_table_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='status',
            field=models.CharField(choices=[('PENDING', 'pending'), ('DELIVERED', 'delivered')], max_length=255, null=True),
        ),
    ]
