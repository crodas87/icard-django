# Generated by Django 4.1.7 on 2023-04-15 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='Sin Nombre', max_length=255)),
                ('direccion', models.CharField(max_length=255, null=True)),
                ('telefono', models.CharField(max_length=20, null=True)),
                ('correo_electronico', models.EmailField(blank=True, max_length=254, null=True)),
                ('sitio_web', models.URLField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('ultima_actualizacion', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
