from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey
from django.forms import model_to_dict
from django.views import *
from django.db import models
from datetime import date
from bases.models import ClaseModelo
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
fpago=[
    ["POR COBRAR", "POR COBRAR"],
    ["CONTADO", "CONTADO"],
    ["CREDITO", "CREDITO"],
    ["PREPAGO", "PREPAGO"],
    ["CREDITO X COBRAR", "CREDITO X COBRAR"],
    ["CONTADO X COBRAR", "CONTADO X COBRAR"],
    ["CREDITO X CREDITO", "CREDITO X CREDITO"],
    ["CORTESIA", "CORTESIA"],
    ["CONTRA ENTREGA", "CONTRA ENTREGA"]
]

class ImpGuias(ClaseModelo):

    fecha = models.DateField(auto_now=False)
    codigo_cliente = models.CharField(max_length=8)
    remitente = models.CharField(max_length=200, verbose_name="Nombre Remitente")
    dirrem = models.CharField(max_length=300, verbose_name="Direccion Remitente")
    tel = models.CharField(max_length=20, verbose_name="No. Telefono")
    zona = models.CharField(max_length=2, verbose_name="Zona")
    muni= models.CharField(max_length=50, verbose_name="Municipio")
    origen = models.CharField(max_length=50, verbose_name="Origen")
    ruta = models.CharField(max_length=3, verbose_name="Ruta")
    #Datos destinatario
    codigo_desti=models.CharField(max_length=8)
    destinatario = models.CharField(max_length=100, verbose_name="Nombre Destinatario", null=True, blank=True)
    dirdes = models.CharField(max_length=300, verbose_name="Direccion Destinatario", null=True, blank=True)
    teldes = models.CharField(max_length=9, verbose_name="No. Telefono", null=True, blank=True)
    zonades = models.CharField(max_length=2, verbose_name="Zona")
    munides= models.CharField(max_length=50, verbose_name="Municipio", null=True, blank=True)
    destino = models.CharField(max_length=50, verbose_name="Codigo Destino", null=True, blank=True)
    rutades = models.CharField(max_length=3, verbose_name="Ruta", null=True, blank=True)
    #Forma de pago 
    fpago= models.CharField(max_length=20, verbose_name="FORMA DE PAGO", null=False)
    #Rango de impresiones
    numini = models.IntegerField(default=0, verbose_name="Numero inicial", unique=True)
    numfin = models.IntegerField(default=0, verbose_name="Numero Final", unique=True)
    totalimp=models.IntegerField(default=0, verbose_name='Total Guías A Imprimir')

    def __str__(self):
        return self.codigo_cliente

    def save(self):
        self.remitente = self.remitente.upper()
        super(ImpGuias, self).save()
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    
    class Meta:
        verbose_name = "Impresion de Guías"
        verbose_name_plural = "Impresiones de Guías"