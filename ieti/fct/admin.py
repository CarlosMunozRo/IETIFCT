from django.contrib import admin
from .models import *

# Register your models here.

class NodoInline(admin.TabularInline):
    model = Nodo
    extra = 1
    ordering = ("orden",)

class NodoPadreAdmin(admin.ModelAdmin):
    inlines = [NodoInline]



admin.site.register(Nodo)
admin.site.register(NodoPadre, NodoPadreAdmin)
#admin.site.register(Orden)