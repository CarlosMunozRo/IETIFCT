from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path('pasos/<int:nodoid>', views.pasos, name='pasos'),
]