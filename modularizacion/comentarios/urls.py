'''Nos tenemso que copiar la estructura porque esta 
esta enfocada en renderizar las vistas de nuestra propia
aplicacion que contiene el modelo de la base de datos'''

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('testapp/', view=views.test, name="test"),
    path('create/', view=views.create,  name="create")
]
