from django.db import models

# Create your models here.


class Coment(models.Model):
    name = models.CharField(max_length=255, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000, null=True)
    date = models.DateField(null=True)
    dia = models.BooleanField(null=True)
    signature = models.CharField(max_length=100, default="FirmaGay")

    def __str__(self):
        return self.name


class Author(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    apellido = models.CharField(max_length=50, null=False)
    segundoApellido = models.CharField(max_length=25, null=False)
