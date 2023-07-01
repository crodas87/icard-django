from rest_framework.routers import DefaultRouter
from proveedores.api.views import ProveedoresApiViewSet

router_proveedores = DefaultRouter()

router_proveedores.register(
    prefix='proveedores', basename='proveedores', viewset=ProveedoresApiViewSet
)
