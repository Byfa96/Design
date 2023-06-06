from django.shortcuts import render, redirect
#from .views import 
from .productos import productos
def mostrar_inicio(request):
    #Se traen los datos a la plantilla
    context = {
        'productos':productos
    }
    return render(request, 'index.html', context)

def mostrar_registro(request):
    return render(request, 'registro.html')