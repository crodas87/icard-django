from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from ingredients.models import Ingredients
from ingredients.api.serializers import IngredientSerializer
from paginacion.paginacion import CustomPagination

from ingredienteProducto.models import IngredienteProducto
from orders.models import Order


class IngredientsApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = IngredientSerializer
    pagination_class = CustomPagination
    queryset = Ingredients.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'proveedor']

    @action(detail=True, methods=['post'])
    def update_stock(self, request):

        idOrder = request.data.get('idOrder')

        try:
            # Obtener el producto asociado a la orden
            order = Order.objects.get(id=idOrder)
            idProducto = order.product.id
            # cantidad de veces que pidio el producto
            quantity = order.quantity
            try:
                # Obtener los ingredientes asociados al producto
                ingredientes_productos = IngredienteProducto.objects.filter(
                    idProducto=idProducto)
                if not ingredientes_productos:
                    return Response({'error': f"No existen ingredientes asignados al Producto con id: {idProducto}"}, status=400)

                for ingrediente_producto in ingredientes_productos:
                    idIngrediente = ingrediente_producto.idIngrediente_id
                    cantidad = ingrediente_producto.cantidad

                    # Calcular la cantidad a descontar del stock
                    cantidad_descontar = cantidad*quantity

                    # Obtener el ingrediente
                    ingrediente = Ingredients.objects.get(id=idIngrediente)

                    # Actualizar el stock del ingrediente
                    ingrediente.stock -= cantidad_descontar
                    ingrediente.save()

                return Response({'message': 'Stock updated successfully'})
            except IngredienteProducto.DoesNotExist:
                return Response({'error': f"No existen ingredientes asignados al Producto con id: {idProducto}"}, status=400)

        except Order.DoesNotExist:
            return Response({'error': 'Order does not exist.'}, status=400)
