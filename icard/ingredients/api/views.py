from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from ingredients.models import Ingredients
from ingredients.api.serializers import IngredientSerializer
from paginacion.paginacion import CustomPagination


class IngredientsApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = IngredientSerializer
    pagination_class = CustomPagination
    queryset = Ingredients.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'proveedor']
