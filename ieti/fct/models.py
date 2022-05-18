from django.db import models
from treebeard.mp_tree import MP_Node
import os
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

def get_temas_images_path(instance, filename):
    return 'temas/{0}/{1}'.format(instance.nombre, filename)

def get_pasos_images_path(instance, filename):
    
    return 'temas/{0}/{1}'.format(instance.nombre, filename)

# Create your models here.
from tinymce import models as tinymce_models

class Tema(models.Model):
    nombre = models.CharField(max_length=200)
    pasoInicial = models.ForeignKey('Paso', on_delete=models.CASCADE, related_name='pasoInicial', null=True, blank=True)

    imagenDestacada = models.ImageField(upload_to=get_temas_images_path, null=True, blank=True)

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

    imagenDestacada = models.ImageField(upload_to=get_pasos_images_path, null=True, blank=True)

    def __str__(self):
        return self.nombre




