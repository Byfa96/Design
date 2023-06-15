from django.shortcuts import render, redirect
#from .views import 
# from .productos import productos
from .forms import NuevoRegistro , FormularioEntrar, FormularioProducto
from django.contrib.auth import authenticate ,logout ,login
from .models import Producto
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from sweetify import info, success, warning, error

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

def carro(request):
    return render(request, 'carrito.html')

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
            return redirect('lista_productos')
    else:
        formulario = FormularioProducto()
    context = {'form': formulario}
    return render(request, 'producto/crear_producto.html', context)



