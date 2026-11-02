from django.http import Http404
from django.shortcuts import render, redirect
from .models import Entrenamiento, Asistencia
from apps.socios.models import Socio

@Login_required
def lista_entrenamientos(request):
    entrenamientos = Entrenamiento.objects.all().order_by('-fecha_hora')
    return render(request, 'entrenamientos/lista.html', {'entrenamientos': entrenamientos})

@Login_required
def crear_entrenamiento(request):
    if request.method == 'POST':
        categoria = request.POST.get('categoria')
        fecha_hora = request.POST.get('fecha_hora')
        lugar = request.POST.get('lugar')

        entrenamiento = Entrenamiento.objects.create(
            categoria=categoria,
            fecha_hora=fecha_hora,
            lugar=lugar
        )
        return redirect('tomar_asistencia', pk=entrenamiento.id)

    return render(request, 'entrenamientos/form.html', {
        'categorias': Socio.CATEGORIAS
    })

@Login_required
def tomar_asistencia(request, pk):
    try:
        entrenamiento = Entrenamiento.objects.get(pk=pk)
    except Entrenamiento.DoesNotExist:
        raise Http404

    jugadores = Socio.objects.filter(categoria=entrenamiento.categoria, activo=True)

    if request.method == 'POST':
        for jugador in jugadores:
            asistio = request.POST.get(f'asistencia_{jugador.id}') == 'on'
            observacion = request.POST.get(f'observacion_{jugador.id}', '')
            
            Asistencia.objects.update_or_create(
                entrenamiento=entrenamiento,
                socio=jugador,
                defaults={'asistio': asistio, 'observacion': observacion}
            )
        return redirect('lista_entrenamientos')

    asistencias_existentes = {a.socio_id: a for a in entrenamiento.asistencias.all()}

    return render(request, 'entrenamientos/asistencia.html', {
        'entrenamiento': entrenamiento,
        'jugadores': jugadores,
        'asistencias_existentes': asistencias_existentes
    })
