from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cuotas, name='lista_cuotas'),
    path('registrar/', views.registrar_pago, name='registrar_pago'),
]