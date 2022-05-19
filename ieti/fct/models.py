from django.db import models
from treebeard.mp_tree import MP_Node
from tinymce import models as tinymce_models
import os




def get_temas_images_path(instance, filename):
    return 'temas/{0}/{1}'.format(instance.nombre, filename)

def get_pasos_images_path(instance, filename):
    
    return 'temas/{0}/{1}'.format(instance.nombre, filename)



class Tema(models.Model):
    nombre = models.CharField(max_length=200)
    pasoInicial = models.ForeignKey('Paso', on_delete=models.CASCADE, related_name='pasoInicial', null=True, blank=True)

    imagenDestacada = models.ImageField(upload_to=get_temas_images_path, null=True, blank=True, max_length=500000)

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

    imagenDestacada = models.ImageField(upload_to=get_pasos_images_path, null=True, blank=True, max_length=255)

    def __str__(self):
        return self.nombre




