
from django.db import models

# Create your models here.
class Pedido_prestamo(models.Model):
    nombre = models.CharField(max_length = 20)
    apellido = models.CharField(max_length = 20)
    dni = models.CharField(max_length = 10)
    genero = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 50)
    monto = models.IntegerField()


class Imagenes(models.Model):
    imagen = models.ImageField(upload_to= 'moniapp')