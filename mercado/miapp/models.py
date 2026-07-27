from django.db import models

class Producto(models.Model):
    nombre = models.DecimalField( max_digits=5, decimal_places=2)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
def __str__(self):
        return self.nombre
