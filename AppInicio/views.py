from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import estudiante
from .forms import estudianteForm



# Create your views here.
def home (request):
    return render(request,'paginas/inicio.html')

def welcome (request):
    return render(request,'paginas/welcome.html')

def estudiantes(request):
    estudiantes = estudiante.objects.all()
    return render(request, 'estudiantes/index.html', {'estudiantes':estudiantes})

def crear(request):
    formulario = estudianteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('estudiantes')
    return render(request,'estudiantes/crear.html', {'formulario':formulario})

def editar(request):
    return render(request,'estudiantes/editar.html')

def aboutus(request):
    return render(request,'estudiantes/nosotros.html')