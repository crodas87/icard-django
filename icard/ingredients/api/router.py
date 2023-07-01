from rest_framework.routers import DefaultRouter

from ingredients.api.views import IngredientsApiViewSet

router_ingredients = DefaultRouter()

router_ingredients.register(
    prefix='ingredients', basename='ingredients', viewset=IngredientsApiViewSet
)
