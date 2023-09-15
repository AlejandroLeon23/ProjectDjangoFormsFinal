# Generated by Django 4.2.5 on 2023-09-15 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promovidos',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=20)),
                ('apellido_materno', models.CharField(max_length=20)),
                ('responsable', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=10)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('municipio', models.CharField(max_length=20)),
                ('colonia', models.CharField(max_length=20)),
                ('calle_y_numero', models.CharField(max_length=40)),
                ('comite', models.CharField(max_length=10)),
                ('seccion', models.CharField(max_length=10)),
                ('latitud', models.CharField(max_length=20)),
                ('longitud', models.CharField(max_length=20)),
            ],
        ),
    ]
