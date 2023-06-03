from django.shortcuts import render

def mostrar_inicio(request):
    return render(request, 'index.html')