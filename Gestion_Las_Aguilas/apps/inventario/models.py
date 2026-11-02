from django.db import models

class MaterialDeportivo(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_total = models.PositiveIntegerField()
    cantidad_disponible = models.PositiveIntegerField()
    estado = models.CharField(max_length=50, default="Buen estado")

    def __str__(self):
        return f"{self.nombre} (Disponibles: {self.cantidad_disponible}/{self.cantidad_total})"

class PrestamoMaterial(models.Model):
    material = models.ForeignKey(MaterialDeportivo, on_delete=models.CASCADE)
    responsable = models.CharField(max_length=100, help_text="Nombre del entrenador o encargado")
    cantidad = models.PositiveIntegerField()
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    devuelto = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.cantidad}x {self.material.nombre} - {self.responsable}"
