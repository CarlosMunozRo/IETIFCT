from django.shortcuts import render
from .models import *

# Create your views here.

def landingPage(request):
    contenido = Abuelo.objects.all()
    contexto = {
        'Contenidos':contenido,
    }
    return render(request,'landingPage.html',contexto)

def pasos(request,nodoid):
    nodo = Abuelo.objects.filter(pk=nodoid)
    contexto = {
        'NodoPadre': nodo,
    }
    return render(request,'wizard.html',contexto)