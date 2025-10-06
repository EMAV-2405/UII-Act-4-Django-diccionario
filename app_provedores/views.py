from django.shortcuts import render

def index(request):
    provedores = [
        {'nombre': 'Proveedor A', 'producto': 'Producto 1', 'contacto': 'contactoA@ejemplo.com'},
        {'nombre': 'Proveedor B', 'producto': 'Producto 2', 'contacto': 'contactoB@ejemplo.com'},
        {'nombre': 'Proveedor C', 'producto': 'Producto 3', 'contacto': 'contactoC@ejemplo.com'},
    ]
   
    return render(request, 'index.html', {'provedores':provedores})