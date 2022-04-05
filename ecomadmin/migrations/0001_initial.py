# Generated by Django 4.0.3 on 2022-04-05 16:38

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClasificacionProducto',
            fields=[
                ('id', models.CharField(max_length=2, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(2)])),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='GrupoProducto',
            fields=[
                ('id_grupo', models.CharField(max_length=2, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(2)])),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LineaProducto',
            fields=[
                ('id', models.CharField(max_length=1, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(1)])),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.CharField(max_length=3, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(3)])),
                ('descripcion', models.CharField(max_length=200)),
                ('clasificacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecomadmin.clasificacionproducto')),
                ('linea', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ecomadmin.lineaproducto')),
            ],
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)])),
                ('descripcion', models.CharField(max_length=200)),
                ('existencia_eu', models.IntegerField(default=0)),
                ('existencia_av', models.IntegerField(default=0)),
                ('existencia_mr', models.IntegerField(default=0)),
                ('existencia_ml', models.IntegerField(default=0)),
                ('precio', models.IntegerField(default=0)),
                ('en_oferta', models.BooleanField(default=False)),
                ('precio_oferta', models.IntegerField(default=0)),
                ('tasa', models.IntegerField(choices=[(0, 0), (5, 5), (10, 10)])),
                ('clasificacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecomadmin.clasificacionproducto')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ecomadmin.grupoproducto')),
                ('linea', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='ecomadmin.lineaproducto')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecomadmin.producto')),
            ],
            options={
                'unique_together': {('grupo', 'codigo')},
            },
        ),
    ]
