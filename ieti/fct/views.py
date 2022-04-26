from django.shortcuts import render
from django.template import loader
from .models import *

# Create your views here.

def landingPage(request):
	return render(request, 'landingPage.html')