from django.forms import ModelForm
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["detalle", "imagen"]
    

