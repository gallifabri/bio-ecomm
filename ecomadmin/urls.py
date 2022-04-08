from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('importacion_de_tablas', views.importacion_de_tablas, name='importacion_de_tablas'),
    path('productos', views.maestro_productos, name='productos'),
    path('productos/presentaciones', views.maestro_presentaciones, name='presentaciones'),
    path('productos/editar/<str:pk>', views.editar_producto.as_view(), name='editar_producto'),
    path('productos/<str:pk>/<str:sk>', views.detalle_presentacion, name='detalle_presentacion'),
    path('productos/<str:pk>', views.detalle_producto, name='detalle_producto'),
    path('tablas/tabla_grupo_productos', views.tabla_grupo_productos, name='tabla_grupo_productos'),
    path('tablas/tabla_linea_productos', views.tabla_linea_productos, name='tabla_linea_productos'),
    path('tablas/tabla_clasificacion_productos', views.tabla_clasificacion_productos, name='tabla_clasificacion_productos'),
]
