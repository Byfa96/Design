from django.shortcuts import render, redirect
#from .views import 
# from .productos import productos
from .models import Producto, Carrito
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

def añadir_carro(request):
    user=request.user
    product_id=request.GET.get('prod_id')
    product = Producto.objects.get(id=product_id)
    Carrito(user=user,product=product).save()
    return redirect("/carrito")

def mostrar_carrito(request):
    user = request.user
    cart = Carrito.objects.filter(user=user)
    return render(request, 'carrito.html', locals())
