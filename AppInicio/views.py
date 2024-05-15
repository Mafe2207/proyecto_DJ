from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return render(request,'paginas/inicio.html')

def welcome (request):
    return render(request,'paginas/welcome.html')

def estudiantes(request):
    return render(request,'estudiantes/index.html')

def crear(request):
    return render(request,'estudiantes/crear.html')