from django.db import models

class Socio(models.Model):
    CATEGORIAS = [  
     ('INF', 'Infantiles / Escuelita'),
     ('M14', 'M14 Juvenil'),
     ('M16', 'M16 Juvenil'),
     ('M18', 'M18 Juvenil'),
     ('PS', 'Plantel Superior'),  
]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    DNI = models.CharField(max_length=15, unique=True)
    Fecha_nacimiento = models.DateField()
    Telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100, unique=True)
    categoria = models.CharField(max_length=3, choices=CATEGORIAS)
    apto_medico_al_dia = models.BooleanField(default=False, verbose_name="Apto Médico URTF")
    activo = models.BooleanField(default=True, verbose_name="Socio Activo")

    def __str__(self):
        return f"{self.apellido}, {self.nombre} ({self.get_categoria_display()})"