from enum import unique
from tabnanny import verbose
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
    (0, "GUIA MADRE"),
    (0, "GUIA HIJA"),
    (0, "GUIA EN BLANCO"),
]

fpago=[
    [0, "POR COBRAR"],
    [1, "CONTADO"],
    [2, "CREDITO"],
    [3, "PREPAGO"],
    [4, "CREDITO X COBRAR"],
    [5, "CONTADO X COBRAR"],
    [6, "CREDITO X CREDITO"],
    [7, "CORTESIA"],
    [8, "TALONARIO"],
]

class GuiasEnv( ClaseModelo):
    fecha = models.DateField(auto_now=True)
    codigo = models.CharField(max_length=9)
    cliente = models.CharField(max_length=300)
    tipo_envio = models.IntegerField(choices=tipo_envio)
    numini = models.IntegerField(default=0, unique=True)
    numfin = models.IntegerField(default=0, unique=True)
    totenvio = models.IntegerField(default=0)
    fpago = models.Index
    entregado = models.BooleanField(default=False)

class Lotes(ClaseModelo):
    no_lote = models.IntegerField(default=0, unique=True)
    fecha = models.DateField(auto_now=True)
    manifiesto_local = models.IntegerField(default=0, null=False, blank=False)
    observaciones = models.TextField(max_length=100)
