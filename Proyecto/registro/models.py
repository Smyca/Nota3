from django.db import models

# Create your models here.
class Registro(models.Model):
    nombre      = models.CharField(max_length=100)
    apellido    = models.CharField(max_length=100)
    email       = models.EmailField()
    password    = models.CharField(max_length=8)