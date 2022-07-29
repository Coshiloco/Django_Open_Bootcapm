
from django.shortcuts import render
from django.db import models
# Create your views here.


def creardatos(request):
    empleadouno = models.objects.create(
    name="Bauty", comment="pablohurtado@gmail.com")
    cargoempleadouno = models.objects.create(empleado=empleadouno,
    headline='Prueba de instanciacion de claves foraneas',
    body_text='Si se crea con exito soy la prueba',
    rating=8)

    resultadobusqueda = models.objects.get(id=1)

    return resultadobusqueda
