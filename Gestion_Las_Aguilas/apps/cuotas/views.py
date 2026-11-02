from django.http import Http404
from django.shortcuts import redirect, render
from .models import Pago_Cuota
from apps.socios.models import Socio
from django.contrib.auth.decorators import login_required

@login_required
def lista_cuotas(request):
    pagos = Pago_Cuota.objects.select_related('socio').order_by('-fecha_pago')
    return render(request, 'cuotas/list.html', {'pagos': pagos})

@login_required
def registrar_pago(request):
    if request.method == 'POST':
        socio_id = request.POST.get('socio')
        mes = request.POST.get('mes')
        anio = request.POST.get('anio')
        monto = request.POST.get('monto')
        medio_pago = request.POST.get('medio_pago')

        try:
            socio = Socio.objects.get(pk=socio_id)
        except Socio.DoesNotExist:
            raise Http404

        Pago_Cuota.objects.create(
            socio=socio,
            mes=mes,
            anio=anio,
            monto=monto,
            medio_pago=medio_pago
        )
        return redirect('lista_cuotas')

    socios = Socio.objects.filter(activo=True).order_by('apellido')
    return render(request, 'cuotas/form.html', {'socios': socios})