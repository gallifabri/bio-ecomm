[1mdiff --cc ecomadmin/models.py[m
[1mindex 6a9ec9f,727add0..0000000[m
[1m--- a/ecomadmin/models.py[m
[1m+++ b/ecomadmin/models.py[m
[36m@@@ -26,15 -26,7 +26,19 @@@[m [mclass ClasificacionProducto(models.Mode[m
  		return f'{self.id} - {self.descripcion}'[m
  [m
  [m
[32m++<<<<<<< HEAD[m
[32m +class Formula(models.Model):[m
[32m +	id = models.CharField(max_length=3, validators=[MinLengthValidator(3)], primary_key=True)[m
[32m +	descripcion = models.CharField(max_length=200)[m
[32m +[m
[32m +[m
[32m +	def __str__(self):[m
[32m +		return f'{self.id} - {self.descripcion}'[m
[32m +[m
[32m +class CatalogoProducto(models.Model):[m
[32m++=======[m
[32m+ class ProductoCatalogo(models.Model):[m
[32m++>>>>>>> 173a619707b3d097b20a7c9b8593aa50e98b8052[m
  	"""[m
  	To do:[m
  	Ver tabla para vincular formulas con presentaciones[m
[36m@@@ -60,13 -52,9 +64,18 @@@[m
  	[m
  [m
  [m
[32m++<<<<<<< HEAD[m
[32m +class PresentacionProducto(models.Model):[m
[32m +	producto = models.ForeignKey(CatalogoProducto, on_delete=models.CASCADE)[m
[32m++=======[m
[32m+ class Producto(models.Model):[m
[32m+ 	producto_catalogo = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True)[m
[32m++>>>>>>> 173a619707b3d097b20a7c9b8593aa50e98b8052[m
  	# presentacion_descripcion [m
[32m +  #	id_formula = models.ForeignKey(Formula, on_delete=models.PROTECT, null=True)[m
[32m +  # presentacion = models.CharField(Formula, max_length=5, validators=[MinLengthValidator(5)])[m
[32m +[m
[32m +[m
  [m
  	# Campos migrados de VFP[m
  	id_grupo = models.ForeignKey(GrupoProducto, on_delete=models.PROTECT)[m
