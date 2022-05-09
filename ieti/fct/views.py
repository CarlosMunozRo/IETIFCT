from http.server import HTTPServer
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
import random

# Create your views here.

def buscar(nodos,nodoPadreId):
    for nodo in nodos:
        
        if nodo['nodoId'] == nodoPadreId:
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

    pasos = Paso.get_annotated_list(Paso.objects.get(id=tema.pasoInicial.id))


    #TEMPORAL
    nextPaso = ""
    prevPaso = ""

    paso_level = 0
    firstLevel = False

    if paso.tipo == 'PR':
        for i in range(len(pasos)):
            if paso.id == pasos[i][0].id:
                try:
                    paso_ = pasos[i+1][0]
                    nextPaso = paso_
                except:
                    pass

                paso_level = pasos[i][1]['level']



            if firstLevel:
                if paso_level == pasos[i][1]['level']:
                    try:
                        paso_ = pasos[i][0]
                        prevPaso = paso_
                    except:
                        pass

            else:
                firstLevel = True

    else:
        for i in range(len(pasos)):
            if paso.id == pasos[i][0].id:
                try:
                    paso_ = pasos[i+1][0]
                    nextPaso = paso_
                except:
                    pass

                
                try:
                    paso_ = pasos[i-1][0]
                    prevPaso = paso_
                except:
                    pass



    contexto = {
        'annotated_list': pasos,
        'paso': paso,
        'tema': tema,
        'adelante': nextPaso,
        'atras': prevPaso,
        'mainChild': tema.pasoInicial,
    }
    return render(request,'wizard.html',contexto)


def login(request):
	return render(request, 'login.html')

