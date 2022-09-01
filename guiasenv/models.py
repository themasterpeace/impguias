from enum import unique
from random import choices
from tabnanny import verbose
from django.urls import reverse, reverse_lazy
from django.forms import model_to_dict
from django.db.models.enums import Choices
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.views import*
from django.db import models
from datetime import datetime 
from bases.models import ClaseModelo


# Create your models here.
TIPO_ENVIO=[
    ("CTE", "CONTRAENTREGA"),
    ("MANI", "MANIFIESTOS"),
    ("GM", "GUIA MADRE"),
    ("GH", "GUIA HIJA"),
    
]

FPAGO=[
    ("XCO", "POR COBRAR"),
    ("CON", "CONTADO"),
    ("CRE", "CREDITO"),
    ("PRE", "PREPAGO"),
    ("COM", "COMPARTIDA"),
    ("COR", "CORTESIA"),
    ("TAL", "TALONARIO"),
    ("GEB", "GUIA EN BLANCO"),
]

class GuiasEnv(models.Model):
    fecha = models.DateField(auto_now=False)
    codigo = models.CharField(max_length=9)
    cliente = models.CharField(max_length=300)
    tipo_envio = models.CharField(max_length=20, choices=TIPO_ENVIO)
    numini = models.IntegerField(default=0, unique=True)
    numfin = models.IntegerField(default=0, unique=True)
    totenvio = models.IntegerField(default=0)
    fpago = models.CharField(max_length=20, choices=FPAGO)
    entregado = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse_lazy("guiasenv:guialist")

    def __str__(self):
        return self.codigo
    
    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    @property
    def tot_envio(self):
        return self.numfin - self.numini + 1
    
    def save(self):
        self.codigo = self.codigo.upper()
        super(GuiasEnv, self).save()

    class Meta:
        verbose_name_plural = "GuiasEnvs"
        ordering = ['id']



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
        verbose_name_plural = "Lote"


