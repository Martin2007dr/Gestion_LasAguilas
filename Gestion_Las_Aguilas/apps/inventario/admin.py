from django.contrib import admin
from .models import MaterialDeportivo, PrestamoMaterial

@admin.register(MaterialDeportivo)
class MaterialDeportivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad_disponible', 'cantidad_total', 'estado')

@admin.register(PrestamoMaterial)
class PrestamoMaterialAdmin(admin.ModelAdmin):
    list_display = ('material', 'responsable', 'cantidad', 'fecha_prestamo', 'devuelto')
    list_filter = ('devuelto',)