from django.http import Http404
from django.shortcuts import redirect, render
from .models import Socio 
from django.contrib.auth.decorators import login_required
@login_required
def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'socios/lista_socios.html', {'socios': socios})

@login_required
def crear_socio(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        DNI = request.POST.get('DNI')
        Fecha_nacimiento = request.POST.get('Fecha_nacimiento')
        Telefono = request.POST.get('Telefono')
        email = request.POST.get('email')
        categoria = request.POST.get('categoria')
        apto_medico_al_dia = request.POST.get('apto_medico_al_dia') == 'on'
        activo = request.POST.get('activo') == 'on'

        Socio.objects.create(
            nombre=nombre,
            apellido=apellido,
            DNI=DNI,
            Fecha_nacimiento=Fecha_nacimiento,
            Telefono=Telefono,
            email=email,
            categoria=categoria,
            apto_medico_al_dia=apto_medico_al_dia,
            activo=activo
        )

        return redirect ('lista_socios')
    return render(request, 'socios/form.html', {
        'titulo': 'Registrar Nuevo Socio',
        'categorias': Socio.CATEGORIAS
    })
@login_required
def editar_socio(request, pk):
    try:
        socio = Socio.objects.get(pk=pk)
    except Socio.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        socio.nombre = request.POST.get('nombre')
        socio.apellido = request.POST.get('apellido')
        socio.DNI = request.POST.get('DNI')
        socio.Fecha_nacimiento = request.POST.get('Fecha_nacimiento')
        socio.Telefono = request.POST.get('Telefono')
        socio.email = request.POST.get('email')
        socio.categoria = request.POST.get('categoria')
        socio.apto_medico_al_dia = request.POST.get('apto_medico_al_dia') == 'on'
        socio.activo = request.POST.get('activo') == 'on'
        socio.save()
        return redirect('lista_socios')

    return render(request, 'socios/form.html', {
        'titulo': f'Editar Socio: {socio.nombre} {socio.apellido}',
        'socio': socio,
        'categorias': Socio.CATEGORIAS
    })

@login_required
def eliminar_socio(request, pk):
    try:
        socio = Socio.objects.get(pk=pk)
    except Socio.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        socio.delete()
        return redirect('lista_socios')
    return render(request, 'socios/confirmar_eliminar.html', {'socio': socio})