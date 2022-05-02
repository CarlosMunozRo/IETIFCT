from django.contrib import admin
from .models import *
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

# Register your models here.

""" class NodoInline(admin.TabularInline):
    model = Nodo
    extra = 1
    ordering = ("orden",)

class NodoPadreAdmin(admin.ModelAdmin):
    inlines = [NodoInline] """


class PasoInline(admin.TabularInline):
    model = Paso


class PasoAdmin(TreeAdmin):
    form = movenodeform_factory(Paso)

admin.site.register(Paso,PasoAdmin)
admin.site.register(Tema)

# admin.site.register(Nodo)
# admin.site.register(NodoPadre, NodoPadreAdmin)
#admin.site.register(Orden)

