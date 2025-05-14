from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Producto, Restaurant
from .forms import ProductoForm
import random
from datetime import datetime
from celery.schedules import crontab
from celery import Celery
from app.tasks import hello_task

def producto_list(request):
    Productos = Producto.objects.all()
    return render(request, 'productos/list.html', {'productos': Productos})

def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto created successfully!')
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'productos/create.html', {'form': form})

def producto_celery(request):
    hello_task.delay()
    return render(request, 'productos/celery.html')

def producto_hilos(request):

    # TODO: Create and run the restaurant system
    menu = ["Pizza", "Pasta", "Salad", "Soup"]
    restaurante = Restaurant()
    restaurante.output.clear()
    restaurante.start_restaurant()

    # Add some example tasks"
    restaurante.create_order(0, random.choice(menu))

    # Wait for all tasks to complete
    restaurante.queue.join()
    restaurante.stop_restaurant()
    restaurante.chef_output()
    return render(request, 'productos/hilos.html', {"restaurante": restaurante.output})

def producto_delete_all(request):
    if request.method == 'POST':
        Producto.objects.all().delete()
    return render(request, 'productos/delete_all.html')

def producto_register(request):
    if request.method == 'GET':
        Productos = Producto.objects.all()
        return render(request, 'productos/register.html', {'productos': Productos})

def producto_pedido(request):
    return render(request, 'productos/pedido.html')
