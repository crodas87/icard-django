from django.contrib import admin

from proveedores.models import Proveedores


@admin.register(Proveedores)
class ProveedoresAdmin(admin.ModelAdmin):
    pass
