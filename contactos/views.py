from django.shortcuts import render
from django.http import HttpResponse
import csv
from .models import Contacto
from .forms import ContactoForm

def lista_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'contactos/lista.html', {'contactos': contactos})

def crear_contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm()
    return render(request, 'contactos/crear.html', {'form': form})

def editar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
    else:
        form = ContactoForm(instance=contacto)
    return render(request, 'contactos/editar.html', {'form': form})

def eliminar_contacto(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos')
    return render(request, 'contactos/eliminar.html', {'contacto': contacto})

# Evidencia técnica: exportar a CSV
def exportar_contactos_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=contactos.csv'
    writer = csv.writer(response)
    writer.writerow(['Nombre', 'Teléfono', 'Email', 'Dirección'])
    for c in Contacto.objects.all().order_by('nombre'):
        writer.writerow([c.nombre, c.telefono, c.email, c.direccion])
    return response
