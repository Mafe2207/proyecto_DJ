from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.home, name='home'),
    path('welcome/', views.welcome, name='welcome'),
    path('estudiantes/', views.estudiantes, name='students'),
    path('estudiantes/crear', views.crear, name='crear'),
    path('estudiantes/editar', views.editar, name='editar'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
