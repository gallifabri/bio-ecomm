from django.forms import ModelForm
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *


class ProductoForm(forms.ModelForm):
    especies = forms.ModelMultipleChoiceField(Especie.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Producto
        fields = ['detalle', 'imagen', 'especies']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields['imagen'].widget)

