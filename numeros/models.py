from django.db import models
from django.utils.timezone import now
from django.conf import settings

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
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    numero = models.ForeignKey('numeros.Numero', related_name='numeros', on_delete=models.CASCADE)
