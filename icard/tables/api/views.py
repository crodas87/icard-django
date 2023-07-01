from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from tables.models import Table
from tables.api.serializers import TableSerializers


class TableApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TableSerializers
    queryset = Table.objects.all().order_by('number')
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['number']
