from django.db import models

# Create your models here.

class Coments(models.Model):
    name = models.CharField(max_length=255, null=False)
    score = models.IntegerField(default=3)
    comment = models.TextField(max_length=1000, null=True)
    def __str__(self):
        return super().__str__()

