from django.db import models
from django.utils.timezone import now

# Create your models here.
class Numero(models.Model):
    titulo = models.TextField(default='',blank=False)
    paginas =  models.IntegerField(default=0, blank=False)
    lanzamiento = models.DateField(default=now, blank=False)
    autor = models.TextField(default='',blank=False)
    clasificacion =  models.IntegerField(default=0, blank=False)
    pais = models.TextField(default='',blank=False)
    genero = models.TextField(default='',blank=False)
    capitulos = models.IntegerField(default=0, blank=False)
    serializacion = models.IntegerField(default=0, blank=False)
    precio = models.FloatField(default=0, blank=False)
