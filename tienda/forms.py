
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import (
    Form,
    CharField,
    PasswordInput,
    EmailField,
    EmailInput,
    Textarea,
    CheckboxInput,
    BooleanField,
    TextInput,
    ModelForm,
    ImageField,
    ClearableFileInput
)
from .models import Producto


class NuevoRegistro(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['password1'].widget.attrs = { 'class':'form-control' }
        self.fields['password2'].widget.attrs = { 'class':'form-control' }
    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'email'
        ]
        widgets = {
            'username': TextInput(
                attrs = {
                    'class':'form-control'
                }
            ),
            'first_name': TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'last_name': TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'email': EmailInput(
                attrs = {
                    'class':'form-control'
                }
            )
        }

class FormularioEntrar(Form):
    usuario = CharField(
        required = True,
        label = 'Ingrese su usuario',
        widget = TextInput(
            attrs = {
                'class' : 'form-control',
                'placeholder':'Ingrese su usuario',
            }
        )
    )
    contrasenia_usuario = CharField(
        required = True,
        min_length = 4,
        max_length= 16,
        label= 'Ingrese su contraseña',
        widget= PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder':'Ingrese su contraseña',
            }
        )
    )

###Futuro formulario de productos

class FormularioProducto(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'img']
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control'}),
            'descripcion': Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': TextInput(attrs={'class': 'form-control'}),
            'img': ClearableFileInput(attrs={'class': 'form-control-file'}),
        }