# Generated by Django 4.1.7 on 2023-03-03 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='totalPayments',
            new_name='totalPayment',
        ),
    ]