from django.db import models

from bases.models import ClaseModelo
# Create your models here.

class Ruta(ClaseModelo):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    ruta = models.CharField(max_length=3)

    def __str__(self):
        return self.nombre

    def save(self):
        self.nombre = self.nombre.upper()
        super(Ruta, self).save()

    class Meta:
        verbose_name_plural = "Rutas"