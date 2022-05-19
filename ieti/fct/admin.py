from django.contrib import admin
from .models import *
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


class PasoInline(admin.TabularInline):
    model = Paso


class PasoAdmin(TreeAdmin):
    form = movenodeform_factory(Paso)

admin.site.register(Paso,PasoAdmin)
admin.site.register(Tema)



