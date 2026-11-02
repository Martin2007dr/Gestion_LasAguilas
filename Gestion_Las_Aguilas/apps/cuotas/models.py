from django.db import models
from apps.socios.models import Socio


class Pago_Cuota(models.Model):
   MEDIOS_PAGO = [
    ('EF', 'Efectivo'),
    ('TR', 'Transferencia'),    
    ('MP', 'Mercado Pago'),
   ]

   MESES = [
    (1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'),
    (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'),
    (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')
   ]
   socio = models.ForeignKey(Socio, on_delete=models.CASCADE, related_name='pagos')
   mes = models.IntegerField(choices=MESES)
   anio = models.IntegerField(default=2026)
   monto = models.DecimalField(max_digits=10, decimal_places=2)
   fecha_pago = models.DateField(auto_now_add=True)
   medio_pago = models.CharField(max_length=2, choices=MEDIOS_PAGO)

   def __str__(self):
    return f"Pago de {self.monto} por {self.socio.nombre} {self.socio.apellido} el {self.fecha_pago}"
