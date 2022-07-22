from django.http import HttpResponse
from django.shortcuts import render
from .models import Coment

# Create your views here.


def test(request):
    return HttpResponse("Funciona correctamente la vista de lo que es la app")


def create(request):
    #pruebacomentario = Coment(name="Bauty", score=100, comment="Bauty es hermoso")
    # Para guardarlo en la base de datos
    # pruebacomentario.save()
    # Otra forma
    comentariodos = Coment.objects.create(
        name="Alejandro", comment="Segunda forma de crear el objeto directamente")
    return HttpResponse("Ruata para probar la creacion de modelos")


def delete(request):
    # Primera forma
    #comment = Coment.objects.get(id=1)
    # comment.delete()
    # Segunda forma
    Coment.objects.filter(id=2).delete()
    return HttpResponse("Ruta para probar el borrado de comentarios")
