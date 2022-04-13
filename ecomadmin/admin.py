from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Presentacion)
admin.site.register(GrupoProducto)
admin.site.register(LineaProducto)
admin.site.register(ClasificacionProducto)
admin.site.register(ImagenProducto)

class ProductoAdmin(admin.ModelAdmin):
    ordering = ['descripcion']

admin.site.register(Producto, ProductoAdmin)


