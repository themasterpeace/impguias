from django.db import models
from django.forms import model_to_dict

from bases.models import ClaseModelo

# Create your models here.

class ImpHija(ClaseModelo):
    madre = models.IntegerField(unique=True)
    pieza = models.IntegerField()
    de = models.IntegerField()
    origen = models.CharField(max_length=3)
    destino = models.CharField(max_length=3)

    def __str__(self):
        return self.origen

    def save(self):
        super(ImpHija, self).save()

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = "ImpHijas"