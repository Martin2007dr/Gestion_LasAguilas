from django.db import models
from apps.socios.models import Socio

class Entrenamiento(models.Model):
    categoria = models.CharField(max_length=5, choices=Socio.CATEGORIAS)
    fecha_hora = models.DateTimeField()
    lugar = models.CharField(max_length=100, default="Cancha Las Águilas")

    def __str__(self):
        return f"Entrenamiento {self.get_categoria_display()} - {self.fecha_hora.strftime('%d/%m/%Y %H:%M')}"

class Asistencia(models.Model):
    entrenamiento = models.ForeignKey(Entrenamiento, on_delete=models.CASCADE, related_name='asistencias')
    socio = models.ForeignKey(Socio, on_delete=models.CASCADE)
    asistio = models.BooleanField(default=False)
    observacion = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.socio} - {self.entrenamiento}"
