from django.shortcuts import render, redirect
#from .views import 
def mostrar_inicio(request):
    return render(request, 'index.html')

def mostrar_registro(request):
    return render(request, 'registro.html')