from django.db import models

from treebeard.mp_tree import MP_Node


# Create your models here.
from tinymce import models as tinymce_models

class Tema(models.Model):
    nombre = models.CharField(max_length=200)
    pasoInicial = models.ForeignKey('Paso', on_delete=models.CASCADE, related_name='pasoInicial', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Paso(MP_Node):
    nombre = models.CharField(max_length=100)
    texto = tinymce_models.HTMLField()
    class TipoNodo(models.TextChoices):
        PREGUNTA = 'PR', 'Pregunta'
        SOLUCION = 'SO', 'Solucion'


    tipo = models.CharField(
        max_length=2,
        choices=TipoNodo.choices,
        default=TipoNodo.PREGUNTA,
    )

    def __str__(self):
        return self.nombre



""" class NodoPadre(models.Model):
    nombre = models.CharField(max_length=50)


    def __str__(self):
        return self.nombre

class Nodo(models.Model):
    nombre = models.CharField(max_length=50)

    nodoPadre = models.ForeignKey('NodoPadre',null=True,blank=True,on_delete=models.CASCADE)
    nodoHijo = models.ManyToManyField('Nodo',null=True,blank=True)

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
        return self.nombre """

""" 
class Orden(models.Model):
    orden = models.IntegerField(default=1)
    nodoPadre = models.ForeignKey('NodoPadre', on_delete=models.CASCADE)
    nodo = models.ForeignKey('Nodo', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.orden) 
"""