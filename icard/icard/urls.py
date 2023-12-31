"""icard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tables.api.router import router_table
from user.api.router import router_user
from categories.api.router import router_category
from products.api.router import router_product
from orders.api.router import router_orders
from payments.api.router import router_payments
from ingredients.api.router import router_ingredients
from proveedores.api.router import router_proveedores
from ingredienteProducto.api.router import router_ingredienteProducto
from ingredienteProducto.api.views import IngredienteProductoApiViewSet
from ingredients.api.views import IngredientsApiViewSet
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('api/', include(router_user.urls)),
    path('api/', include(router_category.urls)),
    path('api/', include(router_product.urls)),
    path('api/', include(router_table.urls)),
    path('api/', include(router_orders.urls)),
    path('api/', include(router_payments.urls)),
    path('api/', include(router_ingredients.urls)),
    path('api/', include(router_proveedores.urls)),
    path('api/', include(router_ingredienteProducto.urls)),
    path('api/', include('user.api.router')),
    path('api/ingredients/update_stock',
         IngredientsApiViewSet.as_view({'post': 'update_stock'}), name='update_stock'),
    path('api/ingredienteProducto/<int:idProducto>/<int:idIngrediente>/',
         IngredienteProductoApiViewSet.as_view({'delete': 'delete_ingrediente_producto'}), name='delete_ingrediente_producto')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
