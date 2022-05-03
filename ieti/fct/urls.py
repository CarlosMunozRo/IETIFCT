from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.landingPage, name='landingPage'),
    path('<int:temaid>/<int:pasoid>', views.pasos, name='pasos'),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='login.html'), name='logout'),
]