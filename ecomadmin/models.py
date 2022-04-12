from django.db import models
from django.core.validators import MinLengthValidator
from ckeditor.fields import RichTextField


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


class Especie(models.Model):
	descripcion = models.CharField(max_length=20, unique=True)

	def get_absolute_url(self):
		return f"especies"

	def __str__(self):
		return self.descripcion


class Producto(models.Model):
	"""
	Crear campos:
		nombre
		sumario
		categoria
		subcategoria (puede ser varios, igual que especies)
	"""    
	# Campos migrados de VFP
	codigo = models.CharField(max_length=3, validators=[MinLengthValidator(3)], primary_key=True)
	descripcion = models.CharField(max_length=200)
	linea = models.ForeignKey(LineaProducto, on_delete=models.PROTECT, null=True) # SET NOT NULL
	clasificacion = models.ForeignKey(ClasificacionProducto, on_delete=models.SET_NULL, null=True)

	# Nuevos campos
	detalle = RichTextField(blank=True, null=True)
	imagen = models.ImageField(upload_to='static/imagenes/',blank=True, null=True)
	especies = models.ManyToManyField(Especie)


	def especies_cs(self):
		return ", ".join([str(especie) for especie in self.especies.all()])

	def __str__(self):
		return f'{self.codigo} - {self.descripcion}'


class Presentacion(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)

	# Campos migrados de VFP
	grupo = models.ForeignKey(GrupoProducto, on_delete=models.PROTECT)
	codigo = models.CharField(max_length=3, validators=[MinLengthValidator(3)])
	descripcion = models.CharField(max_length=200)
	existencia_eu = models.IntegerField(default=0)
	existencia_av = models.IntegerField(default=0)
	existencia_mr = models.IntegerField(default=0)
	existencia_ml = models.IntegerField(default=0)
	precio = models.IntegerField(default=0)
	en_oferta = models.BooleanField(default=False)
	precio_oferta = models.IntegerField(default=0)
	tasa = models.IntegerField(choices=[(0,0),(5,5),(10,10)])
	linea = models.ForeignKey(LineaProducto, on_delete=models.PROTECT, null=True) # SET NOT NULL
	clasificacion = models.ForeignKey(ClasificacionProducto, on_delete=models.SET_NULL, null=True)

	class Meta:
		unique_together = (('grupo', 'codigo'),)

	def __str__(self):
		return f'{self.grupo.id_grupo}{self.codigo} - {self.descripcion}'


