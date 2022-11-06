from django.db import models


# Create your models here.
class MisFamiliares(models.Model):
    nombre = models.CharField(max_length=25)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

