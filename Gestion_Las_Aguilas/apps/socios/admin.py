from django.contrib import admin
from .models import Socio


@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'DNI', 'categoria', 'activo')
    search_fields = ('apellido', 'nombre', 'DNI')
    list_filter = ('categoria', 'activo')
