from django.http import HttpResponse
from django.shortcuts import render
from .models import Cargo, Empleado
# Create your views here.


def creardatos(request):
    empleadouno = Empleado.objects.create(
    name="Bauty", email="pablohurtado@gmail.com")
    cargoempleadouno = Cargo.objects.create(empleado=empleadouno,
    headline='Prueba de instanciacion de claves foraneas',
    body_text='Si se crea con exito soy la prueba',
    rating=8)

    resultadobusqueda = Empleado.objects.get(id=1)
    
    return HttpResponse(f"{resultadobusqueda}")
