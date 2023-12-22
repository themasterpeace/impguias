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
    ("CONTRA ENTREGA", "CONTRA ENTREGA"),
    ("MANIFIESTOS", "MANIFIESTOS"),
    ("GUIA MADRE", "GUIA MADRE"),
    ("GUIA HIJA", "GUIA HIJA"),
    
]

FPAGO=[
    ("POR COBRAR", "POR COBRAR"),
    ("CONTADO", "CONTADO"),
    ("CREDITO", "CREDITO"),
    ("PREPAGO", "PREPAGO"),
    ("COMPARTIDA", "COMPARTIDA"),
    ("CORTESIA", "CORTESIA"),
    ("TALONARIO", "TALONARIO"),
    ("GUIA EN BLANCO", "GUIA EN BLANCO"),
]

class Cliente(ClaseModelo):
    codigo = models.CharField(max_length=8)
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    #nit = models.CharField(max_length=10)
    #departamento = models.CharField(max_length=50)
    municipio = models.CharField(max_length=150)
    #contacto = models.CharField(max_length=150)
    formapago = models.CharField(max_length=20,choices=FPAGO)

    def get_absolute_url(self):
        return reverse_lazy("guiasenv:clientelist")

    def __str__(self):
        return self.codigo

    def save(self):
        self.nombre = self.nombre.upper()
        super(Cliente, self).save()
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = "Clientes"
        ordering = ['id'] 

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
    observaciones = models.TextField(max_length=200)

    def __str__(self):
        return '{}'.format(self.no_lote)
    
    def save(self):
        self.no_lote = self.no_lote.upper()
        super(Lote, self).save()

    class Meta:
        verbose_name_plural = "Lotes"


