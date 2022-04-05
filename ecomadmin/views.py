from django.shortcuts import render
from .models import *
from .servicios import *
from .forms import *
from django.shortcuts import get_object_or_404

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
	presentaciones = None

	if Presentacion.objects.filter(producto=producto).exists():
		presentaciones = Presentacion.objects.filter(producto=producto)

	context = {'producto': producto, 'collapse' : 'producto', 'presentaciones' : presentaciones}

	return render(request, 'detalle_producto.html', context=context)


def editar_producto(request, pk):
	producto = get_object_or_404(Producto, codigo=pk)
	form = ProductoForm(instance=producto)

	context = {'form' : form}
	
	return render(request, 'editar_producto.html', context=context)



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



  