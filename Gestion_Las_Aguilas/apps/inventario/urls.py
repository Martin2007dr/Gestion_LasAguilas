from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_inventario, name='lista_inventario'),
    path('nuevo/', views.crear_material, name='crear_material'),
    path('prestamo/', views.registrar_prestamo, name='registrar_prestamo'),
    path('devolver/<int:pk>/', views.devolver_material, name='devolver_material'),
]