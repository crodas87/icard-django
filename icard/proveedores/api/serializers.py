from rest_framework.serializers import ModelSerializer
from proveedores.models import Proveedores


class ProveedoresSerializer(ModelSerializer):
    class Meta:
        model = Proveedores
        fields = ['id', 'nombre', 'direccion', 'telefono',
                  'correo_electronico', 'sitio_web',]
