from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('estudiantes/', views.estudiantes, name='students'),
    path('estudiantes/crear', views.crear, name='crear'),
]
