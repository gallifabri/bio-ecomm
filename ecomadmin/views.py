from django.shortcuts import render
from .models import *
from .servicios import *
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

	return render(request, 'importacion_de_tablas.html', context={})


def maestro_producto(request):
	grupos = GrupoProducto.objects.all().order_by('id_grupo')
	grupo = request.GET.get('grupo', '')

	if grupo == "":
		productos = Producto.objects.all().values('grupo__id_grupo', 'id_producto', 'descripcion')
	else:
		productos = Producto.objects.filter(grupo__id_grupo=grupo).values('grupo__id_grupo', 'id_producto', 'descripcion')

	context = {'productos' : productos, 'grupo' : grupo, 'grupos' : grupos}

	return render(request, 'maestro_producto.html', context=context)


def detalle_producto(request, pk, sk):
	producto = get_object_or_404(Producto, grupo=GrupoProducto.objects.get(id_grupo=pk), id_producto=sk)
	context = {'producto': producto}

	return render(request, 'detalle_producto.html', context=context)


def tabla_grupo_productos(request):
	grupos = GrupoProducto.objects.all().order_by('id_grupo')
	context = {'grupos' : grupos}

	return render(request, 'tabla_grupo_productos.html', context=context)


def tabla_linea_productos(request):
	lineas = LineaProducto.objects.all().order_by('id')
	context = {'lineas' : lineas}

	return render(request, 'tabla_linea_productos.html', context=context)


def tabla_clasificacion_productos(request):
	clasificaciones = ClasificacionProducto.objects.all().order_by('id')
	context = {'clasificaciones' : clasificaciones}

	return render(request, 'tabla_clasificacion_productos.html', context=context)

def tabla_formula_presentacion(request):
	formula = Formula.objects.all().order_by('id_formula')
	context = {'formula' : formula}

	return render(request, 'tabla_formula_presentacion.html', context=context)

  