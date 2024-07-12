from django.shortcuts import render, redirect
from .models import Productos
from .Carrito import Carrito

def carta (request):
    productos = Productos.objects.all()
    return render(request, 'carta.html', {'productos' : productos})

def agregar_producto (request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id = producto_id)
    carrito.agregar(producto)
    return redirect('carta')

def eliminar_producto (request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id = producto_id)
    carrito.eliminar(producto)
    return redirect('carta')

def restar_producto (request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(id = producto_id)
    carrito.restar(producto)
    return redirect('carta')

def limpiar_carrito (request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('carta')
