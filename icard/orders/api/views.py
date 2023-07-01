
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from datetime import datetime
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from orders.models import Order
from rest_framework import pagination
from orders.api.serializers import OrderSerializer
from paginacion.paginacion import CustomPagination


class OrderFilter(filters.FilterSet):
    start_date = filters.DateFilter(
        field_name='created_at', lookup_expr='date__gte')
    end_date = filters.DateFilter(
        field_name='created_at', lookup_expr='date__lte')

    class Meta:
        model = Order
        fields = ['table', 'status', 'payment', 'close',
                  'product', 'start_date', 'end_date']


class OrderApiViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = OrderFilter
    ordering_fields = '__all__'
    pagination_class = CustomPagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('start_date', openapi.IN_QUERY,
                              description="Start date for filtering", type=openapi.TYPE_STRING),
            openapi.Parameter('end_date', openapi.IN_QUERY,
                              description="End date for filtering", type=openapi.TYPE_STRING),
        ]
    )
    def list(self, request, *args, **kwargs):
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        queryset = self.filter_queryset(self.get_queryset())

        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()

            queryset = queryset.filter(
                created_at__date__range=(start_date, end_date))

        # Obtener el valor del parámetro de página
        page_number = request.query_params.get('page')

        if page_number is not None:
            page_number = int(page_number)

            paginator = CustomPagination()

            # Aplicar paginación personalizada si se proporciona el parámetro "page"
            paginated_queryset = paginator.paginate_queryset(
                queryset, request=request)  # Modificación aquí

            serializer = self.get_serializer(paginated_queryset, many=True)
            return paginator.get_paginated_response(serializer.data)

        # Si no se proporciona el parámetro "page", devolver todos los datos sin paginación
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
