from django.contrib import admin
from .models import Entrenamiento, Asistencia

@admin.register(Entrenamiento)
class EntrenamientoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'fecha_hora', 'lugar')
    list_filter = ('categoria', 'fecha_hora')

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('entrenamiento', 'socio', 'asistio')
    list_filter = ('asistio',)