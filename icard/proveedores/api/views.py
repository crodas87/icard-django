from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


from proveedores.models import Proveedores
from proveedores.api.serializers import ProveedoresSerializer


class ProveedoresApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ProveedoresSerializer
    queryset = Proveedores.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre']
