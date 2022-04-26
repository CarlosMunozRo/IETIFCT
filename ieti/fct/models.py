from django.db import models

# Create your models here.

class Abuelo(models.Model):
    texto = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)