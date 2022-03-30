from dbfread import DBF
from .models import *


def eliminar_todo_productos():
	Producto.objects.all().delete()


def parse_fecha(fecha):
	if fecha == '':
		return None
	return f'{fecha[:4]}-{fecha[4:6]}-{fecha[6:]}'

	
def leer_campo_numerico_con_null(entrada, leyenda):
	return entrada[leyenda] if entrada[leyenda] is not None else 0


def cargar_tabla_productos():
	
	grupos = GrupoProducto.objects.all()
	grupos_dict = {grupo.id_grupo : grupo for grupo in grupos}
	lineas = LineaProducto.objects.all()
	lineas_dict = {linea.id : linea for linea in lineas}
	clasificaciones = ClasificacionProducto.objects.all()
	clasificaciones_dict = {clasificacion.id : clasificacion for clasificacion in clasificaciones}
	clasificaciones_dict[''] = None
		
	records = [Producto(grupo=grupos_dict[record['CODGRUPO']],
						linea=lineas_dict[record['LINEA']],
						id_producto=record['PRODUCTO'], 
						descripcion=record['DESCRIP'],		
						existencia_eu=leer_campo_numerico_con_null(record, 'EXISTENEU'),
						existencia_av=leer_campo_numerico_con_null(record, 'EXISTENAV'),
						existencia_mr=leer_campo_numerico_con_null(record, 'EXISTENMR'),
						existencia_ml=leer_campo_numerico_con_null(record, 'EXISTENML'),
						precio=record['VENTA1'],
						en_oferta=(True if record['OFERTA'] == 'S' else False),
						tasa=record['TASA'],
						clasificacion=clasificaciones_dict[record['CLASIFICA']],				
						precio_oferta=leer_campo_numerico_con_null(record, 'VTAOFERTA'),
						)
				for record in DBF('tablas/producto.dbf')]

	Producto.objects.bulk_create(records)


def cargar_tabla_formula():
	ProductoCatalogo.objects.all().delete()

	for record in DBF('tablas/formucab.dbf'):
		nuevo_producto_catalogo = ProductoCatalogo.objects.create()
		nuevo_producto_catalogo.codigo_formula = record['CODFORMULA']
		nuevo_producto_catalogo.descripcion = record['DESCFORMU']
		nuevo_producto_catalogo.save()

		for col in ['PRESEN2', 'PRESEN3', 'PRESEN4', 'PRESEN5']:
			presen = record[col]
			cod_grupo = presen[:2]
			cod_producto = presen[2:]

			if presen != '' and Producto.objects.filter(grupo=cod_grupo, id_producto=cod_producto).exists():
				producto = Producto.objects.get(grupo=cod_grupo, id_producto=cod_producto)

				producto.producto_catalogo = nuevo_producto_catalogo
				producto.save()


def cargar_grupo_productos():
	for record in DBF('tablas/grupopro.dbf'):
		id_grupo = record['CODIGO']
		descripcion = record['DESCRIP2']

		if not GrupoProducto.objects.filter(id_grupo=id_grupo).exists():
			GrupoProducto.objects.create(id_grupo=id_grupo, descripcion=descripcion)


def importar_dbf_linea_producto():
	for record in DBF('tablas/lineacod.dbf'):
		id = record['LINEA']
		descripcion = record['DESCRIP']

		if not LineaProducto.objects.filter(id=id).exists():
			LineaProducto.objects.create(id=id, descripcion=descripcion)


def importar_dbf_clasificacion_producto():
	for record in DBF('tablas/precigan.dbf'):
		id = record['CODIGO']
		descripcion = record['DESCRIP']

		if not ClasificacionProducto.objects.filter(id=id).exists():
			ClasificacionProducto.objects.create(id=id, descripcion=descripcion)


