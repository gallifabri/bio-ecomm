from django.forms import ModelForm, Form
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import *

from django.utils.safestring import mark_safe
from django import forms

class ImagePreviewWidget(forms.widgets.ClearableFileInput):
	def render(self, name, value, attrs=None, **kwargs):
		input_html = super().render(name, value, attrs=None, **kwargs)
		if value:
			img_html = mark_safe(f'<img style="width: 100px" src="{value.url}"/><br><br>')
			return f'{img_html}{input_html}'
		return input_html


class ProductoForm(forms.ModelForm):
	especies = forms.ModelMultipleChoiceField(Especie.objects.all(), widget=forms.CheckboxSelectMultiple)

	class Meta:
		model = Producto
		fields = ['detalle', 'imagen', 'especies']
		widgets = {
			'imagen': ImagePreviewWidget(),
		}






