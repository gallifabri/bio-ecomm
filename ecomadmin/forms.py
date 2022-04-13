from django.forms import ModelForm, Form
from django import forms
from django.db import models

from ckeditor.widgets import CKEditorWidget
from .models import *

from django.utils.safestring import mark_safe
from django import forms

class ImagePreviewWidget(forms.widgets.FileInput):
	def render(self, name, value, attrs=None, **kwargs):
		input_html = super().render(name, value, attrs=None, **kwargs)
		if value:
			if hasattr(value, 'url'):
				img_html = mark_safe(f'<img style="width: 100px" src="{value.url}"/><br><br><span>Modificar: </span>')
				return f'{img_html}{input_html}'
		return input_html


class ProductoForm(forms.ModelForm):
	especies = forms.ModelMultipleChoiceField(Especie.objects.all(), widget=forms.CheckboxSelectMultiple)

	class Meta:
		model = Producto
		fields = ['detalle', 'especies']
		widgets = {
		}

	def __init__(self, *args, **kwargs):
		super(ProductoForm, self).__init__(*args, **kwargs)
		self.fields['especies'].required = False



class ImagenForm(forms.ModelForm):
	class Meta:
		model = ImagenProducto
		fields = ['producto', 'imagen', ]
		widgets = {
			'imagen': ImagePreviewWidget(),
		}






