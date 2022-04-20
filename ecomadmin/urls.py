from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('importacion_de_tablas', views.importacion_de_tablas, name='importacion_de_tablas'),
    path('productos', views.maestro_productos, name='productos'),
    path('productos/presentaciones', views.maestro_presentaciones, name='presentaciones'),
    path('productos/editar/<str:pk>', views.editar_producto, name='editar_producto'),
    path('productos/<str:pk>/<str:sk>', views.detalle_presentacion, name='detalle_presentacion'),
    path('productos/<str:pk>', views.detalle_producto, name='detalle_producto'),
    path('tablas/grupo_productos', views.tabla_grupo_productos, name='tabla_grupo_productos'),
    path('tablas/linea_productos', views.tabla_linea_productos, name='tabla_linea_productos'),
    path('tablas/clasificacion_productos', views.tabla_clasificacion_productos, name='tabla_clasificacion_productos'),
    path('tablas/especies', views.tabla_especies, name='tabla_especies'),
    path('tablas/crear', views.EspecieCreateView.as_view(), name='tabla_especies_crear'),
    path('tablas/editar/<str:pk>', views.EspecieUpdateView.as_view(), name='tabla_especies_editar'),
    path('tablas/eliminar/<str:pk>', views.EspecieDeleteView.as_view(), name='tabla_especies_eliminar'),
    path('tablas/subcategoria', views.tabla_subcategoria, name='tabla_subcategoria'),
    path('tablas/crear_subcategoria', views.SubcategoriaCreateView.as_view(), name='tabla_subcategoria_crear'),
    path('tablas/editar_subcategoria/<str:pk>', views.SubcategoriaUpdateView.as_view(), name='tabla_subcategoria_editar'),
    path('tablas/eliminar_subcategoria/<str:pk>', views.SubcategoriaDeleteView.as_view(), name='tabla_subcategoria_eliminar'),
]
