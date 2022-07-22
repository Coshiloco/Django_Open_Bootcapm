from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def test(request):
  return HttpResponse("Funciona correctamente la vista de lo que es la app")
