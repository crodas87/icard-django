from django.db import models


class Proveedores(models.Model):
    nombre = models.CharField(max_length=255, default="Sin Nombre")
    direccion = models.CharField(max_length=255, null=True)
    telefono = models.CharField(max_length=20, null=True)
    correo_electronico = models.EmailField(blank=True, null=True)
    sitio_web = models.URLField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre
