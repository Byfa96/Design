from django.db import models
from django.contrib.auth.models import User
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    precio_des = models.FloatField()
    img = models.ImageField(upload_to="comida", blank=True)

class Carrito(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    

    @property
    def costo_total(self):
        return self.quantity * self.product.precio
