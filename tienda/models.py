from django.db import models
from django.contrib.auth.models import User
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    img = models.ImageField(upload_to="comida", blank=True)

class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, default=0)

class EntradaCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
