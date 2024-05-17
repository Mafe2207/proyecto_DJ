from django.shortcuts import render
from django.http import HttpResponse
from .models import estudiante


# Create your views here.
def home (request):
    return render(request,'paginas/inicio.html')

def welcome (request):
    return render(request,'paginas/welcome.html')

def estudiantes(request):
    estudiantes = estudiante.objects.all()
    return render(request, 'estudiantes/index.html', {'estudiantes':estudiantes})

def crear(request):
    return render(request,'estudiantes/crear.html')

def editar(request):
    return render(request,'estudiantes/editar.html')