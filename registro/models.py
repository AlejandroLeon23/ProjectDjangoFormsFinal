from django.db import models

# Create your models here.
class Promovidos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    responsable = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    correo_electronico = models.EmailField()
    municipio = models.CharField(max_length=20)
    colonia = models.CharField(max_length=20)
    calle_y_numero = models.CharField(max_length=40)
    comite = models.CharField(max_length=10)
    seccion = models.CharField(max_length=10)
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)

    def __str__(self):
        return self.nombres
