from django.http import HttpResponse
from django.shortcuts import render
from .models import Coment
# Create your views here.


def creardatos(request):
    empleadouno = Coment.objects.create(
    name="Bauty", comment="pablohurtado@gmail.com")
    cargoempleadouno = Coment.objects.create(empleado=empleadouno,
    headline='Prueba de instanciacion de claves foraneas',
    body_text='Si se crea con exito soy la prueba',
    rating=8)

    resultadobusqueda = Coment.objects.get(id=1)

    return resultadobusqueda
