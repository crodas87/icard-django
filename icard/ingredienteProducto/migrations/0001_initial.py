# Generated by Django 4.1.7 on 2023-04-27 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0006_remove_product_producttype'),
        ('ingredients', '0009_remove_ingredients_quantity_ingredients_um'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredienteProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=0, default=0.0, max_digits=10)),
                ('IdIngrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ingredients.ingredients')),
                ('idProducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]