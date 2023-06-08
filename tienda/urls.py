from django.contrib import admin
from django.urls import path
from .views import mostrar_inicio, mostrar_registro, mostrar_login, salir
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', mostrar_inicio, name='inicio'),
    #Login y registro
    path('registro/', mostrar_registro, name='registro'),
    path('inicio_sesion/', mostrar_login, name='login'),
    path('salir/', salir, name='salir'),
    #
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)