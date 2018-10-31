from django.shortcuts import redirect, render,get_object_or_404
from django.utils import timezone
from .models import Adoptar, Adoptado
from .forms import AdoptarForm, AdoptadoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

def index(request):
    adoptar = Adoptar.objects.order_by('run')
    adoptados = Adoptado.objects.order_by('nombre')
    return render(request, 'Perris/index.html', {'adoptantes': adoptar, 'adoptados': adoptados})

def galeria(request):
    PerriDisponibles = Adoptado.objects.filter(estado__contains='Disponible')
    PerriRescatados = Adoptado.objects.filter(estado__contains='Rescatado')
    PerriAdoptados = Adoptado.objects.filter(estado__contains='Adoptado')
    return render(request, 'Perris/galeria.html',{'PerriDisponibles': PerriDisponibles, 'PerriAdoptados': PerriAdoptados ,'PerriRescatados': PerriRescatados})


@login_required
def adoptar(request):
    if request.method == "POST":
        form = AdoptarForm(request.POST)
        if form.is_valid():
            Adoptar = form.save(commit=False)
            Adoptar.save()
            return redirect('perritos_disponibles')
    else:
        form = AdoptarForm()
    return render(request, 'Perris/adopta.html',{'form': form})


def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        ...

@login_required
def perritos_disponibles(request):
    PerriDisponibles = Adoptado.objects.filter(estado__contains='Disponible')
    return render(request, 'Perris/galeriaDisponible.html', {'PerriDisponibles': PerriDisponibles})

def perritos_rescatados(request):
    PerriRescatados = Adoptado.objects.filter(estado__contains='Rescatado')
    return render(request, 'Perris/galeriaRescatado.html', {'PerriRescatados': PerriRescatados})

def perritos_adoptados(request):
    PerriAdoptados = Adoptado.objects.filter(estado__contains='Adoptado')
    return render(request, 'Perris/galeriaAdoptado.html', {'PerriAdoptados': PerriAdoptados})

@login_required
def detalle_perro(request, pk):
    adoptado = get_object_or_404(Adoptado, pk=pk)
    return render(request, 'Perris/detalle_perro.html',{'adoptado': adoptado})

@login_required
def adoptar_perro(request, pk):
    adoptado = get_object_or_404(Adoptado, pk=pk)
    if request.method == "POST":
        form = AdoptadoForm(request.POST, instance=adoptado)
        if form.is_valid():
            adoptado = form.save(commit=False)
            adoptado.save()
            return redirect('galeria')
    else:
        form = AdoptadoForm(instance=adoptado)
    return render(request, 'Perris/adoptar_perro.html', {'form': form, 'adoptado': adoptado})

