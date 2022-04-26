from django.db import models

# Create your models here.
from tinymce import models as tinymce_models

class TipoNodo(models.Model):
    nombre = models.CharField(max_length=50)



class Nodo(models.Model):
    tipo = models.ForeignKey('TipoNodo', on_delete=models.CASCADE)
    texto= tinymce_models.HTMLField()
    hijo = models.ManyToManyField('self', null=True, blank=True)
    siguiente = models.ManyToManyField('self', null=True, blank=True)
    ordern = models.IntegerField(default=1)

    
    
class Abuelo(models.Model):
    texto = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    def __str__(self):
        return self.texto
