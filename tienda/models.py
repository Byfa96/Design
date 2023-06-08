from django.db import models
from django.contrib.auth.models import User
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    img = models.ImageField(upload_to="comida", blank=True)


