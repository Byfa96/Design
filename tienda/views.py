from django.shortcuts import render, redirect
#from .views import 
# from .productos import productos
from .models import Producto
def mostrar_inicio(request):
    #Se traen los datos a la plantilla
    productos = Producto.objects.all()
    backup = productos
    if request.method == 'GET':
        ingresado = request.GET.get('buscador')

        if ingresado:
            backup = []
            for producto in productos:
                if ingresado.lower() in producto.nombre.lower():
                    backup.append(producto)
    context = {
        'productos':backup
    }
    return render(request, 'index.html', context)

def mostrar_registro(request):
    return render(request, 'registro.html')

def mostrar_carrito(request):
    return render(request, 'carrito.html')
