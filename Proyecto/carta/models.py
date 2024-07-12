from django.db import models

class Productos (models.Model) :
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    imagen = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.nombre)