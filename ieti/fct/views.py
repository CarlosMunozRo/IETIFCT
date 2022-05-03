from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def landingPage(request):
    contenido = NodoPadre.objects.all()
    contexto = {
        'Contenidos':contenido,
    }
    return render(request,'landingPage.html',contexto)

def pasos(request,nodoid):
    nodo = NodoPadre.objects.filter(pk=nodoid)
    contexto = {
        'NodoPadre': nodo,
    }
    return render(request,'wizard.html',contexto)


def login(request):
	return render(request, 'login.html')