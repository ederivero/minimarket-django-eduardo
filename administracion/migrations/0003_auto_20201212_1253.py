# Generated by Django 3.1.4 on 2020-12-12 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_auto_20201212_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='productomodel',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='almacenmodel',
            name='almacenDescripcion',
            field=models.CharField(db_column='alma_desc', help_text='aca va la descripcion del almacen', max_length=75, verbose_name='Descripcion del almacen'),
        ),
    ]
