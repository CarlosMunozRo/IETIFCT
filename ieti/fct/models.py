from django.db import models

# Create your models here.
from tinymce import models as tinymce_models


class NodoPadre(models.Model):
    nombre = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre

class Nodo(models.Model):
    nombre = models.CharField(max_length=50)

    nodoPadre = models.ForeignKey('NodoPadre',null=True,blank=True,on_delete=models.CASCADE)
    nodoPadrePadre = models.ForeignKey('Nodo',null=True,blank=True,on_delete=models.CASCADE)

    class TipoNodo(models.TextChoices):
        PREGUNTA = 'PR', 'Pregunta'
        SOLUCION = 'SO', 'Solucion'


    tipo = models.CharField(
        max_length=2,
        choices=TipoNodo.choices,
        default=TipoNodo.PREGUNTA,
    )

    texto= tinymce_models.HTMLField()
    orden = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

""" 
class Orden(models.Model):
    orden = models.IntegerField(default=1)
    nodoPadre = models.ForeignKey('NodoPadre', on_delete=models.CASCADE)
    nodo = models.ForeignKey('Nodo', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.orden) 
"""