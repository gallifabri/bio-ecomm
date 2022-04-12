from django.forms import ModelForm
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *


class ProductoForm(forms.ModelForm):
    especies = forms.ModelMultipleChoiceField(Especie.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Producto
        fields = ['detalle', 'imagen', 'especies']
    

