from django.contrib import admin
from django.urls import path
from .views import mostrar_inicio, mostrar_registro, mostrar_carrito, añadir_carro
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', mostrar_inicio, name='inicio'),
    path('registro/', mostrar_registro, name='registro'),
    path('añadir/', añadir_carro, name='añadir'),
    path('carrito/', mostrar_carrito, name='carrito'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)