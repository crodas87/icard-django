from rest_framework.serializers import ModelSerializer
from tables.models import Table


class TableSerializers(ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'number']
