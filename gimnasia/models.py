import datetime

from django.db import models
from django.utils import timezone



class Navbar(models.Model):
    navbar_item = models.CharField(max_length=200)
    navbar_item_href_url = models.CharField(max_length=200)
    def __str__(self):
        return self.navbar_item


class Entrenador(models.Model):
    entrenador_nombre = models.CharField(max_length=200)
    entrenador_descripcion = models.CharField(max_length=1000)
    fecha_de_ingreso = models.DateTimeField('date published')
    def __str__(self):
        return self.entrenador_nombre
    def was_published_recently(self):
        return self.fecha_de_ingreso >= timezone.now() - datetime.timedelta(days=1)