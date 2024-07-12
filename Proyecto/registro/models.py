from django.db import models

# Create your models here.
class Registro(models.Model):
    nombre      = models.CharField(max_length=100)
    apellido    = models.CharField(max_length=100)
    email       = models.EmailField()
    password    = models.CharField(max_length=8)

    def __str__(self):
        return str(self.nombre)+' '+str(self.apellido)