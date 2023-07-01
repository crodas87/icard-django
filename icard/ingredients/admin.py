from django.contrib import admin
from ingredients.models import Ingredients

from django.contrib import admin
from ingredients.models import Ingredients


@admin.register(Ingredients)
class IngredientAdmin(admin.ModelAdmin):
    pass
