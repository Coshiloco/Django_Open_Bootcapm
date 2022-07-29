from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('testapp/', view=views.creardatos, name='testapp')
]