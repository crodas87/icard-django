from rest_framework.serializers import ModelSerializer

from products.models import Product
from categories.api.serializers import CategorySerializer, ModelSerializer


class ProductSerializer(ModelSerializer):
    category_data = CategorySerializer(source='category', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'image', 'codbarra',
                  'price', 'active', 'category', 'category_data', 'ingredientes']
