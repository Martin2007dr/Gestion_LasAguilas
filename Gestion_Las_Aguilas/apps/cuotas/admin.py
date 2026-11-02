from django.contrib import admin
from .models import Pago_Cuota


@admin.register(Pago_Cuota)
class PagoCuotaAdmin(admin.ModelAdmin):
    list_display = ('socio', 'mes', 'anio', 'monto', 'medio_pago', 'fecha_pago')
    list_filter = ('mes', 'anio', 'medio_pago')
    search_fields = ('socio__apellido', 'socio__nombre', 'socio__DNI')
