from rest_framework.serializers import ModelSerializer

from ingredients.models import Ingredients
from categories.api.serializers import CategorySerializer, ModelSerializer
from proveedores.api.serializers import ProveedoresSerializer, ModelSerializer


class IngredientSerializer(ModelSerializer):
    category_data = CategorySerializer(source='category', read_only=True)
    proveedores_data = ProveedoresSerializer(
        source='proveedor', read_only=True)

    class Meta:
        model = Ingredients
        fields = ['id', 'title', 'image', 'um',
                  'price', 'stock', 'category', 'category_data', 'proveedor', 'proveedores_data']
