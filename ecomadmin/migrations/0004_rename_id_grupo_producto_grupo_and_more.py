# Generated by Django 4.0.3 on 2022-03-30 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomadmin', '0003_formula'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='id_grupo',
            new_name='grupo',
        ),
        migrations.AlterUniqueTogether(
            name='producto',
            unique_together={('grupo', 'id_producto')},
        ),
    ]
