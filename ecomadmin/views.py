from .models import *
from .servicios import *
from .forms import *
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import modelformset_factory, inlineformset_factory, HiddenInput, BaseInlineFormSet


# Create your views here.
def index(request):
	return render(request, 'index.html', context={})


def importacion_de_tablas(request):
	if request.method == 'POST':
		if request.POST.get('clase') == 'producto':
			cargar_tabla_productos()
		elif request.POST.get('clase') == 'borrar_productos':
			eliminar_todo_productos()
		elif request.POST.get('clase') == 'cargar_formula':
			cargar_tabla_formula()	
		elif request.POST.get('clase') == 'grupo_producto':
			cargar_grupo_productos()
		elif request.POST.get('clase') == 'linea_producto':
			importar_dbf_linea_producto()
		elif request.POST.get('clase') == 'clasificacion_producto':
			importar_dbf_clasificacion_producto()

	return render(request, 'importacion_de_tablas.html', context={'tab' : 'migraciones'})


def maestro_presentaciones(request):
	grupos = GrupoProducto.objects.all().order_by('id_grupo')
	grupo = request.GET.get('grupo', '')

	if grupo == "":
		presentaciones = Presentacion.objects.all().values('grupo__id_grupo', 'codigo', 'descripcion')
	else:
		presentaciones = Presentacion.objects.filter(grupo__id_grupo=grupo).values('grupo__id_grupo', 'codigo', 'descripcion')

	context = {'presentaciones' : presentaciones, 'grupo' : grupo, 'grupos' : grupos, 'collapse' : 'producto'}

	return render(request, 'maestro_presentaciones.html', context=context)


def detalle_presentacion(request, pk, sk):
	presentacion = get_object_or_404(Presentacion, grupo=GrupoProducto.objects.get(id_grupo=pk), codigo=sk)
	context = {'presentacion': presentacion, 'collapse' : 'producto'}

	return render(request, 'detalle_presentacion.html', context=context)


def maestro_productos(request):
	productos = Producto.objects.all().values('codigo', 'descripcion')
	
	context = {'productos' : productos, 'collapse' : 'producto'}

	return render(request, 'maestro_productos.html', context=context)


def detalle_producto(request, pk):
	producto = get_object_or_404(Producto, codigo=pk)
	imagenes = ImagenProducto.objects.filter(producto=producto).exclude(imagen='')
	presentaciones = None

	if Presentacion.objects.filter(producto=producto).exists():
		presentaciones = Presentacion.objects.filter(producto=producto)

	context = {'producto': producto, 'collapse' : 'producto', 'presentaciones' : presentaciones, 'imagenes' : imagenes}

	return render(request, 'detalle_producto.html', context=context)

# class ImagenFormSet(BaseModelFormSet):
#     def clean(self):
#         super(ImagenFormSet, self).clean()

#         years = []
#         for form in self.forms:
#             year = form.cleaned_data['year']
#             years.append(year)
#         if years.count(2017) > 12:
#             raise forms.ValidationError('You selected more than 12 months for 2017')





def editar_producto(request, pk):
	producto = get_object_or_404(Producto, codigo=pk)
	num_imgs = ImagenProducto.objects.filter(producto=producto).count()
	ImagenFormset = inlineformset_factory(Producto, 
											ImagenProducto, 
											fields=('imagen',),
											max_num=10,
											extra=10,
											widgets={'imagen' : ImagePreviewWidget,},
											)

	if request.method == 'POST':
		form = ProductoForm(request.POST, request.FILES, instance=producto)
		formset = ImagenFormset(request.POST, request.FILES, instance=producto)

		if form.is_valid() and formset.is_valid():
			form.save()
			formset.save()

			return HttpResponseRedirect(reverse('detalle_producto', args=[producto.codigo]) )

	else:
		formset = ImagenFormset(instance=producto)
		form = ProductoForm(instance=producto)


	context = {'form': form, 'producto': producto, 'formset': formset, 'count' : num_imgs}
	
	return render(request, 'editar_producto.html', context=context)


############## TABLAS ##################

def tabla_grupo_productos(request):
	grupos = GrupoProducto.objects.all().order_by('id_grupo')
	context = {'grupos' : grupos, 'collapse' : 'tablas'}

	return render(request, 'tabla_grupo_productos.html', context=context)


def tabla_linea_productos(request):
	lineas = LineaProducto.objects.all().order_by('id')
	context = {'lineas' : lineas, 'collapse' : 'tablas'}

	return render(request, 'tabla_linea_productos.html', context=context)


def tabla_clasificacion_productos(request):
	clasificaciones = ClasificacionProducto.objects.all().order_by('id')
	context = {'clasificaciones' : clasificaciones, 'collapse' : 'tablas'}

	return render(request, 'tabla_clasificacion_productos.html', context=context)


def tabla_especies(request):
	especies = Especie.objects.all().order_by('descripcion')
	context = {'especies' : especies, 'collapse' : 'tablas'}

	return render(request, 'tabla_especies.html', context=context)


class EspecieCreateView(CreateView):
	model = Especie
	fields = ['descripcion']
	context = {'collapse' : 'tablas'}
	template_name = "especie_form.html"


class EspecieUpdateView(UpdateView):
	model = Especie
	fields = ['descripcion']
	template_name_suffix = '_update_form'
	context = {'collapse' : 'tablas'}
	template_name = "especie_update_form.html"
	success_url = reverse_lazy('tabla_especies')

  
class EspecieDeleteView(DeleteView):
	model = Especie
	success_url = reverse_lazy('tabla_especies')
	context = {'collapse' : 'tablas'}
	template_name = "especie_confirm_delete.html"


def tabla_subcategoria(request):
	subcategoria = Subcategoria.objects.all().order_by('descripcion')
	context = {'subcategoria' : subcategoria, 'collapse' : 'tablas'}

	return render(request, 'tabla_subcategoria.html', context=context)


class SubcategoriaCreateView(CreateView):
	model = Subcategoria
	fields = ['descripcion']
	context = {'collapse' : 'tablas'}
	template_name = "subcategoria_form.html"


class SubcategoriaUpdateView(UpdateView):
	model = Subcategoria
	fields = ['descripcion']
	template_name_suffix = '_update_form'
	context = {'collapse' : 'tablas'}
	template_name = "subcategoria_update_form.html"
	success_url = reverse_lazy('tabla_subcategoria')

  
class SubcategoriaDeleteView(DeleteView):
	model = Subcategoria
	success_url = reverse_lazy('tabla_subcategoria')
	context = {'collapse' : 'tablas'}
	template_name = "subcategoria_confirm_delete.html"