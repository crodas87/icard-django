from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponseServerError


from ingredienteProducto.models import IngredienteProducto
from ingredienteProducto.api.serializers import IngredienteProductoSerializer


class IngredienteProductoApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = IngredienteProductoSerializer
    queryset = IngredienteProducto.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['idProducto']

    @action(detail=True, methods=['delete'])
    def delete_ingrediente_producto(self, request, idProducto, idIngrediente):
        # Busca el objeto IngredienteProducto por los valores de idProducto e idIngrediente
        ingrediente_producto = get_object_or_404(
            IngredienteProducto, idProducto=idProducto, idIngrediente=idIngrediente)

        try:
            # Borra el objeto IngredienteProducto de la base de datos
            ingrediente_producto.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'detail': 'Error al borrar el IngredienteProducto: {}'.format(str(e))},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
