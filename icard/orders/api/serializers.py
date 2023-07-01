from itertools import product
from rest_framework.serializers import ModelSerializer

from orders.models import Order
from products.api.serializers import ProductSerializer
from tables.api.serializers import TableSerializers


class OrderSerializer(ModelSerializer):
    product_data = ProductSerializer(source='product', read_only=True)
    table_data = TableSerializers(source='table', read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'status', 'table', 'table_data', 'product', 'product_data','quantity','payment', 'close', 'created_at']