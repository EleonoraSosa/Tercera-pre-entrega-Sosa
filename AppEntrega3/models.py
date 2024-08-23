from django.db import models

# Create your models here.


class Registro(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    edad = models.IntegerField()
   

class Ubicacion(models.Model):
    ciudad = models.CharField(max_length=40)
    capital = models.CharField(max_length=40)
    codigo_postal = models.IntegerField()

class Pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=10)
    año = models.IntegerField()
