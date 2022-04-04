from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('importacion_de_tablas', views.importacion_de_tablas, name='importacion_de_tablas'),
    path('productos', views.maestro_producto, name='productos'),
    path('productosgenericos', views.maestro_producto_generico, name='maestro_producto_generico'),
    path('productos/<str:pk>/<str:sk>', views.detalle_producto, name='detalle_producto'),
    path('productos/<str:pk>', views.detalle_producto_generico, name='detalle_producto_generico'),
    path('tablas/tabla_grupo_productos', views.tabla_grupo_productos, name='tabla_grupo_productos'),
    path('tablas/tabla_linea_productos', views.tabla_linea_productos, name='tabla_linea_productos'),
    path('tablas/tabla_clasificacion_productos', views.tabla_clasificacion_productos, name='tabla_clasificacion_productos'),
]
