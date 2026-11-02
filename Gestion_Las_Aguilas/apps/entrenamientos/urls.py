from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_entrenamientos, name='lista_entrenamientos'),
    path('crear/', views.crear_entrenamiento, name='crear_entrenamiento'),
    path('<int:pk>/asistencia/', views.tomar_asistencia, name='tomar_asistencia'),
]