from django.http import HttpResponse
from django.shortcuts import render
from .models import Coment

# Create your views here.

def test(request):
  return HttpResponse("Funciona correctamente la vista de lo que es la app")
  
  
def create(request):
  pruebacomentario = Coment(name="Bauty", score=100, comment="Bauty es hermoso")
  #Para guardarlo en la base de datos 
  pruebacomentario.save()
  return HttpResponse("Ruata para probar la creacion de modelos")
