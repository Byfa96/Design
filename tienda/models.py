from django.db.models import (Model, 
                              CharField, 
                              TextField, 
                              DecimalField, 
                              ImageField, 
                              ForeignKey, 
                              CASCADE)


from django.contrib.auth.models import User

class Producto(Model):
    nombre = CharField(max_length=100)
    descripcion = TextField()
    precio = DecimalField(max_digits=8, decimal_places=2)
    img = ImageField(upload_to="comida", blank=True)
    usuario = ForeignKey(User, on_delete = CASCADE)