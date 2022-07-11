
from django import forms


class FormPedido_prestamo(forms.Form):

    nombre = forms.CharField(label = 'Nombre', max_length = 20)
    apellido = forms.CharField(label = 'Apellido', max_length = 20)
    dni = forms.CharField(label = 'Dni', max_length = 10)
    genero = forms.CharField(label = 'Genero', max_length = 10)
    email = forms.EmailField(label = 'Email', max_length = 50)
    monto = forms.IntegerField(label = 'monto')

