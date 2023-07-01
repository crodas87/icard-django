from rest_framework import serializers


from ingredienteProducto.models import IngredienteProducto
from products.api.serializers import ProductSerializer
from ingredients.api.serializers import IngredientSerializer


class IngredienteProductoSerializer(serializers.ModelSerializer):
    producto_data = ProductSerializer(source='idProducto', read_only=True)
    ingrediente_data = IngredientSerializer(
        source='idIngrediente', read_only=True)

    class Meta:
        model = IngredienteProducto
        fields = ['idProducto', 'producto_data',
                  'idIngrediente', 'ingrediente_data', 'cantidad']
