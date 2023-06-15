from django.contrib import admin
from django.urls import path
from .views import (mostrar_inicio, 
                    mostrar_registro, 
                    mostrar_producto,
                    mostrar_login, 
                    salir, 
                    carro,
                    listar_producto,
                    crear_producto)
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', mostrar_inicio, name='inicio'),
    #Login y registro
    path('registro/', mostrar_registro, name='registro'),
    path('inicio_sesion/', mostrar_login, name='login'),
    path('salir/', salir, name='salir'),
    path('carro/', carro, name='carro'),
    path('producto/', mostrar_producto, name='producto'),
    path('listar_producto/', listar_producto, name='listar_producto' ),
    path('crear_producto/', crear_producto, name='crear_producto')
    #
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)