from django.forms import ModelForm
from .models import *

# Create the form class.
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'descripcion', 'linea', 'clasificacion']
