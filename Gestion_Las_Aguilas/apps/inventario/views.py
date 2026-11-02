from django.shortcuts import render, redirect, get_object_or_404
from .models import MaterialDeportivo, PrestamoMaterial

@Login_required
def lista_inventario(request):
    materiales = MaterialDeportivo.objects.all()
    prestamos = PrestamoMaterial.objects.filter(devuelto=False).order_by('-fecha_prestamo')
    return render(request, 'inventario/lista.html', {
        'materiales': materiales,
        'prestamos': prestamos
    })

@Login_required
def crear_material(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cantidad = int(request.POST.get('cantidad_total'))
        estado = request.POST.get('estado')

        MaterialDeportivo.objects.create(
            nombre=nombre,
            cantidad_total=cantidad,
            cantidad_disponible=cantidad,
            estado=estado
        )
        return redirect('lista_inventario')

    return render(request, 'inventario/form_material.html')

@Login_required
def registrar_prestamo(request):
    if request.method == 'POST':
        material_id = request.POST.get('material')
        responsable = request.POST.get('responsable')
        cantidad = int(request.POST.get('cantidad'))

        material = MaterialDeportivo.objects.get(id=material_id)
        if cantidad <= material.cantidad_disponible:
            PrestamoMaterial.objects.create(
                material=material,
                responsable=responsable,
                cantidad=cantidad
            )
            material.cantidad_disponible -= cantidad
            material.save()

        return redirect('lista_inventario')

    materiales = MaterialDeportivo.objects.filter(cantidad_disponible__gt=0)
    return render(request, 'inventario/form_prestamo.html', {'materiales': materiales})

@Login_required
def devolver_material(request, pk):
    prestamo = get_object_or_404(PrestamoMaterial, pk=pk)
    if not prestamo.devuelto:
        prestamo.devuelto = True
        prestamo.save()

        
        material = prestamo.material
        material.cantidad_disponible += prestamo.cantidad
        material.save()

    return redirect('lista_inventario')
