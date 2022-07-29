from datetime import date
from django.db import models

# Create your models here.
class Empleado(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    # CUando se consulte nos va a devolver el nombre del autor
    def __str__(self):
        return self.name


class Cargo(models.Model):
    # Clave foranea campo foreing key y entre parentesis la clase de la que queremos que nos guarde la clave foranea
    '''CUando eliminemos un autor como esta en cascada
    lo que le estamos diciendo es que tambien nos elimine a su vez
    la entrada para que no haya incoherencias
    y se lo especificamos con el on_delete=en Cascade'''
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    public_date = models.DateField(default=date.today)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline