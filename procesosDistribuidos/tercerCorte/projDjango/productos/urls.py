from django.urls import path
from .views import (
    producto_list,
    producto_create,
    producto_celery,
    producto_hilos,
    producto_delete_all,
    producto_register,
    producto_pedido
)

urlpatterns = [
    path('', producto_list, name='producto_list'),
    path('create/', producto_create, name='producto_create'),
    path('celery/', producto_celery, name='producto_celery'),
    path('hilos/', producto_hilos, name='producto_hilos'),
    path('delete_all/', producto_delete_all, name='producto_delete_all'),
    path('register/', producto_register, name='producto_register'),
    path('lista_pedidos/', producto_pedido, name='producto_pedido')
]