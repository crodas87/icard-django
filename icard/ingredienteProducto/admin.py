from django.contrib import admin

from ingredienteProducto.models import IngredienteProducto


@admin.register(IngredienteProducto)
class IngredienteProductoAdmin(admin.ModelAdmin):
    pass
