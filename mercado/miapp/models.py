from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique= True)
    slug = models.SlugField(unique=True)
    def __str__(self):
                return self.nombre

class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nombre"]
        def __str__(self):
            return self.nombre

class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="productos",
        null=True,
        blank=True,
    )


    nombre = models.CharField( max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion =  models.TextField()
    stock = models.IntegerField()
    marca = models.CharField(max_length=100, default= 0)
    imagen = models.ImageField(upload_to="productos/" , null=True, blank=True)

    def __str__(self):
        return self.nombre
