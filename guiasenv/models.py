from enum import unique
from random import choices
from tabnanny import verbose
from django.urls import reverse, reverse_lazy
from django.db.models.enums import Choices
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.views import*
from django.db import models
from datetime import datetime 
from bases.models import ClaseModelo


# Create your models here.
tipo_envio=[
    (0, "CONTRAENTREGA"),
    (1, "MANIFIESTOS"),
    (2, "GUIA MADRE"),
    (3, "GUIA HIJA"),
    
]

fpago=[
    [0, "POR COBRAR"],
    [1, "CONTADO"],
    [2, "CREDITO"],
    [3, "PREPAGO"],
    [4, "CONTADO X COBRAR"],
    [5, "CREDITO X CREDITO"],
    [6, "CORTESIA"],
    [7, "TALONARIO"],
    (8, "GUIA EN BLANCO"),
    (9, "COMPARTIDA"),
]

class GuiasEnv(models.Model):
    fecha = models.DateField(auto_now=False)
    codigo = models.CharField(max_length=9)
    cliente = models.CharField(max_length=300)
    tipo_envio = models.IntegerField(choices=tipo_envio)
    numini = models.IntegerField(default=0, unique=True)
    numfin = models.IntegerField(default=0, unique=True)
    totenvio = models.IntegerField(default=0)
    fpago = models.IntegerField(choices=fpago)
    entregado = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse_lazy("guiasenv:guialist")

    def __str__(self):
        return '{}'.format(self.codigo)
    
    def save(self):
        self.codigo = self.codigo.upper()
        super(GuiasEnv, self).save()

    class Meta:
        verbose_name_plural = "GuiasEnvs"



class Lote(models.Model):
    no_lote = models.IntegerField(default=0, unique=True)
    fecha = models.DateField(auto_now=True)
    manifiesto_local = models.IntegerField(default=0, null=False, blank=False)
    observaciones = models.TextField(max_length=100)

    def __str__(self):
        return '{}'.format(self.no_lote)
    
    def save(self):
        self.no_lote = self.no_lote.upper()
        super(Lote, self).save()

    class Meta:
        verbose_name_plural = "Lotes"


