from django.db import models


class Ingredients(models.Model):

    title = models.CharField(max_length=255)
    image = models.CharField(max_length=250, null=True, blank=True)
    um = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0.0)
    stock = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    category = models.ForeignKey(
        'categories.Category', on_delete=models.SET_NULL, null=True, blank=True)
    proveedor = models.ForeignKey(
        'proveedores.Proveedores', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
