from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return HttpResponse("Bienvenidos a App Inicio")

def welcome (request):
    return render(request,'paginas/welcome.html')

