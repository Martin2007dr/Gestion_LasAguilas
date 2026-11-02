# core/views.py
from django.shortcuts import render
from apps.socios.models import Socio
from apps.cuotas.models import Pago_Cuota
from apps.entrenamientos.models import Entrenamiento

@Login_required
def home(request):
    total_socios = Socio.objects.filter(activo=True).count()
    socios_sin_apto = Socio.objects.filter(activo=True, apto_medico_al_dia=False).count()
    ultimos_pagos = Pago_Cuota.objects.select_related('socio').order_by('-fecha_pago')[:5]
    proximos_entrenamientos = Entrenamiento.objects.order_by('-fecha_hora')[:3]
    
    context = {
        'total_socios': total_socios,
        'socios_sin_apto': socios_sin_apto,
        'ultimos_pagos': ultimos_pagos,
        'proximos_entrenamientos': proximos_entrenamientos,
    }
    return render(request, 'home.html', context)