from django.forms import ModelForm
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *

# Create the form class.
#class ProductoForm(ModelForm):
#    class Meta:
#        model = Producto
#        fields = ['codigo', 'descripcion', 'linea', 'clasificacion', 'detalle']

class ProductoForm(forms.ModelForm):
    detalle = forms.CharField(widget = CKEditorWidget())
    class Meta:
        model = Producto
        fields = "__all__"
