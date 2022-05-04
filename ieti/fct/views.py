from http.server import HTTPServer
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def buscar(nodos,nodoPadreId):
    for nodo in nodos:
        
        if nodo['nodoId'] == nodoPadreId:
            print(nodo['hijos'], " ",nodoPadreId)
            return nodo['hijos']
        else:
            if buscar(nodo['hijos'],nodoPadreId)==True:
                return False
        

def landingPage(request):
    contenido = Tema.objects.all()


    contexto = {
        'Contenidos':contenido,
    }


    return render(request,'landingPage.html',contexto)

def pasos(request,temaid,pasoid):


    try:
        tema = Tema.objects.get(id=temaid)
    except:
        return HttpResponse("No existe el tema")


    try:
        paso = Paso.objects.get(id=pasoid)
    except:
        return HttpResponse("El tema not tiene paso inicial")


    contexto = {
        'annotated_list': Paso.get_annotated_list(Paso.objects.get(id=tema.pasoInicial.id)),
        'paso': paso,
        'tema': tema,
    }
    return render(request,'wizard.html',contexto)


def login(request):
	return render(request, 'login.html')

