from django.db import models


class Product(models.Model):

    title = models.CharField(max_length=255)
   # image = models.ImageField(upload_to='products')
    image = models.CharField(max_length=250, null=True, blank=True)
    # stock = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    codbarra = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0.0)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(
        'categories.Category', on_delete=models.SET_NULL, null=True, blank=True)
    ingredientes = models.ManyToManyField(
        'ingredients.Ingredients', through='ingredienteProducto.IngredienteProducto')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title
