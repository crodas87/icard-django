from django.db import models

# Create your models here.


class IngredienteProducto(models.Model):
    idProducto = models.ForeignKey(
        'products.Product', on_delete=models.CASCADE)
    idIngrediente = models.ForeignKey(
        'ingredients.Ingredients', on_delete=models.CASCADE)
    cantidad = models.DecimalField(
        max_digits=10, decimal_places=0, default=0.0)

    class Meta:
        unique_together = ('idProducto', 'idIngrediente')

    def __str__(self):
        return f"{self.idProducto.title} usa {self.cantidad} de {self.idIngrediente.title}"
