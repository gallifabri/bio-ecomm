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
    # detalle = forms.CharField(widget = CKEditorWidget())

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)

        self.fields['linea'].widget.attrs['value'] = self.instance.linea
        self.fields['linea'].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = Producto
        fields = "__all__"
    codigo = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))





    # class Meta:
    #     model = Users
    #     fields = ['email', 'first_name', 'last_name', 'birth_date']
    # email = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
