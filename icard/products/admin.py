from django.contrib import admin
from products.models import Product
from ingredienteProducto.models import IngredienteProducto
# Register your models here.


class IngredienteProductoInline(admin.TabularInline):
    model = IngredienteProducto


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        IngredienteProductoInline,
    ]
