from django.db import models


# Create your models here.

class Proyecto(models.Model):
    numero = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=5)
    region = models.CharField(max_length=255)
    titular = models.CharField(max_length=255)
    tipologia = models.CharField(max_length=255)
    inversion = models.CharField(max_length=255)
    fecha = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)

