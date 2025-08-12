from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacto

def lista_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'lista_contactos.html', {'contactos': contactos})

def nuevo_contacto(request):
    if request.method == 'POST':
        Contacto.objects.create(
            nombre=request.POST['nombre'],
            telefono=request.POST['telefono'],
            email=request.POST['email']
        )
        return redirect('lista_contactos')
    return render(request, 'nuevo_contacto.html')

def editar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        contacto.nombre = request.POST['nombre']
        contacto.telefono = request.POST['telefono']
        contacto.email = request.POST['email']
        contacto.save()
        return redirect('lista_contactos')
    return render(request, 'editar_contacto.html', {'contacto': contacto})

def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    contacto.delete()
    return redirect('lista_contactos')
