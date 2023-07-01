from rest_framework.routers import DefaultRouter

from ingredienteProducto.api.views import IngredienteProductoApiViewSet

router_ingredienteProducto = DefaultRouter()

router_ingredienteProducto.register(
    prefix='ingredienteProducto', basename='ingredienteProducto', viewset=IngredienteProductoApiViewSet

)
