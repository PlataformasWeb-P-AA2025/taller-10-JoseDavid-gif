from django.shortcuts import render, redirect
from .models import Parroquia, Barrio
from .forms import ParroquiaForm, BarrioForm

def listar_parroquias_y_barrios(request):
    parroquias = Parroquia.objects.prefetch_related('barrios').all()
    return render(request, 'ordenamiento/parroquias_y_barrios.html', {'parroquias': parroquias})

def listar_barrios(request):
    barrios = Barrio.objects.select_related('parroquia').all()
    return render(request, 'ordenamiento/listar_barrios.html', {'barrios': barrios})

# Función para crear parroquia
def crear_parroquia(request):
    if request.method == 'POST':
        form = ParroquiaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_parroquias_y_barrios')
    else:
        form = ParroquiaForm()
    return render(request, 'ordenamiento/form_parroquia.html', {'form': form})

# Función para crear barrio
def crear_barrio(request):
    if request.method == 'POST':
        form = BarrioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_barrios')
    else:
        form = BarrioForm()
    return render(request, 'ordenamiento/form_barrio.html', {'form': form})