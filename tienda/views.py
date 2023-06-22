from django.shortcuts import render, redirect
#from .views import 
# from .productos import productos
from .forms import NuevoRegistro , FormularioEntrar, FormularioProducto
from django.contrib.auth import authenticate ,logout ,login
from .models import Producto
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from sweetify import info, success, warning, error
###
from .models import Producto, InventarioCompra
from django.contrib.auth.models import User
###
def mostrar_inicio(request):
    return render(request, 'index.html')

def mostrar_producto(request):
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
    return render(request, 'producto.html', context)

###Temas de registro y inicio de sesión

def mostrar_registro(request):
    if request.method == 'GET':
        contexto = {
            'formulario': NuevoRegistro()
        }
        return render(request, 'registro.html', contexto)
    if request.method == 'POST':
        formulario_registro = NuevoRegistro(data=request.POST)
        es_valido = formulario_registro.is_valid() # Retorna un bool
        if es_valido: # Si bool es True
            usuario_nuevo = formulario_registro.save()
            success(request,'Gracias por registrarte!')
            return redirect('inicio')
        contexto = {
            'formulario': formulario_registro
        }
        warning(request, 'Campos invalidos')
        return render(request,'registro.html',contexto)
    
def mostrar_login(request):
    if request.method == 'GET':
        contexto = {
            'titulo': 'Bienvenido',
            'formulario':FormularioEntrar()
        }
        return render(request,'login.html',contexto)
    if request.method == 'POST':
        datos_usuario = FormularioEntrar(data = request.POST)
        es_valido = datos_usuario.is_valid()
        if es_valido:
            usuario = authenticate(username = datos_usuario.cleaned_data['usuario'], 
            password = datos_usuario.cleaned_data['contrasenia_usuario']
            )
            if usuario is not None:
                login(request, usuario)
                success(request, 'Ingreso correctamente')
                return redirect('inicio')
        warning(request, 'Usuario o contraseña invalidos')
        contexto = {
            'formulario': datos_usuario
        }
        return render(request, 'login.html',contexto)

def salir(request):
    if request.user.is_authenticated:
        logout(request)
        success(request, 'Sesión cerrada correctamente')
    return redirect('inicio')

###Fin login/register/logout

#################
def carro(request):
    lista = []
    if request.user.is_authenticated:
        try:
            user = User.objects.get(username=request.user.username)
        except User.DoesNotExist:
            user = None
        if user is None:
            return render(request, 'carrito.html')
        
        try:
            existe = InventarioCompra.objects.filter(id_usuario=request.user.id)
        except InventarioCompra.DoesNotExist:
            existe = None
        
        if existe is None:
            return render(request, 'carrito.html')
        else:
            for i in existe:
                prod = Producto.objects.get(nombre = i.id_producto.nombre)
                dic = {
                    'producto': prod.nombre,
                    'cantidad': i.cantidad,
                    'precio': prod.precio * i.cantidad
                }
                lista.append(dic)
            
            cont = {
                'producto': lista
            }
            
            return render(request, 'carrito.html', cont)
    else:
        return render(request, 'carrito.html')
    


def borrar_carro(request):
    prod = Producto.objects.get(nombre = request.POST.get('nombre'))
    InventarioCompra.objects.get(id_producto = prod).delete()
    return redirect('carro')


def borrar_todo_carro(request):
    InventarioCompra.objects.filter(id_usuario = request.user).delete()
    success(request, 'carrito limpiado')
    return redirect('carro')

def crear_inventario(request):
    inventario = InventarioCompra.objects.create(
        id_usuario = request.user,
        id_producto = Producto.objects.get(nombre = request.POST.get('nombre')),
        cantidad = 1
            )
            
    inventario.save()
    return redirect('producto')

##################################

def listar_producto(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'producto/listar_producto.html', context)

def crear_producto(request):
    if request.method == 'POST':
        formulario = FormularioProducto(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            success(request, 'Producto añadido correctamente')
            return redirect('listar_producto')
    else:
        formulario = FormularioProducto()
    context = {'form': formulario}
    return render(request, 'producto/crear_producto.html', context)

def eliminar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    success(request, 'Producto eliminado correctamente')
    return redirect('listar_producto')

def editar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)

    if request.method == 'POST':
        formulario = FormularioProducto(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            success(request, 'Producto actualizado correctamente')
            return redirect('listar_producto')
    else:
        formulario = FormularioProducto(instance=producto)

    context = {'form': formulario}
    return render(request, 'producto/editar_producto.html', context)






