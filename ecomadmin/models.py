from django.db import models
from django.core.validators import MinLengthValidator


class GrupoProducto(models.Model):
	id_grupo = models.CharField(max_length=2, validators=[MinLengthValidator(2)], primary_key=True)
	descripcion = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.id_grupo} - {self.descripcion}'


class LineaProducto(models.Model):
	id = models.CharField(max_length=1, validators=[MinLengthValidator(1)], primary_key=True)
	descripcion = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.id} - {self.descripcion}'


class ClasificacionProducto(models.Model):
	id = models.CharField(max_length=2, validators=[MinLengthValidator(2)], primary_key=True)
	descripcion = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.id} - {self.descripcion}'



class ProductoCatalogo(models.Model):
	"""
	To do:
	Ver tabla para vincular formulas con presentaciones

	Crear campos:
	nombre
	sumario
	especies
	categoria
	subcategoria (puede ser varios, igual que especies)

	detalle (text field)


	"""
   

	# Campos migrados de VFP
	linea = models.ForeignKey(LineaProducto, on_delete=models.PROTECT, null=True) # SET NOT NULL
	clasificacion = models.ForeignKey(ClasificacionProducto, on_delete=models.SET_NULL, null=True)


	



class Producto(models.Model):
	producto_catalogo = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)
	# presentacion_descripcion 
  #	id_formula = models.ForeignKey(Formula, on_delete=models.PROTECT, null=True)
  # presentacion = models.CharField(Formula, max_length=5, validators=[MinLengthValidator(5)])



	# Campos migrados de VFP
	id_grupo = models.ForeignKey(GrupoProducto, on_delete=models.PROTECT)
	id_producto = models.CharField(max_length=3, validators=[MinLengthValidator(3)])
	nombre_sis = models.CharField(max_length=200)
	existencia_eu = models.IntegerField(default=0)
	existencia_av = models.IntegerField(default=0)
	existencia_mr = models.IntegerField(default=0)
	existencia_ml = models.IntegerField(default=0)
	precio = models.IntegerField(default=0)
	en_oferta = models.BooleanField(default=False)
	precio_oferta = models.IntegerField(default=0)
	tasa = models.IntegerField(choices=[(0,0),(5,5),(10,10)])


	class Meta:
		unique_together = (('id_grupo', 'id_producto'),)

	def __str__(self):
		return self.descripcion


