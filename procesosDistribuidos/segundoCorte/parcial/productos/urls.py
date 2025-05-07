from django.urls import path
from .views import producto_list, producto_create, producto_celery, producto_hilos

urlpatterns = [
    path('', producto_list, name='producto_list'),
    path('create/', producto_create, name='producto_create'),
    path('celery/', producto_celery, name='producto_celery'),
    path('hilos/', producto_hilos, name='producto_hilos'),
]