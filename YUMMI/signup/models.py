from django.db import models
    
class register (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=8)