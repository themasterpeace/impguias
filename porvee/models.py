import datetime
from django.db import models
from django.forms import model_to_dict

from bases.models import ClaseModelo
# Create your models here.

class Proveedor(ClaseModelo):
    nit=models.IntegerField(unique=True, verbose_name="Nit")
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=9)
    contacto=models.CharField(max_length=200)    

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        super(Proveedor, self).save()
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name_plural = "Proveedores"
        ordering = ['id'] 

class Factura(ClaseModelo):
    prove=models.ForeignKey(Proveedor, on_delete=models.PROTECT)
    nombre= models.CharField(max_length=200)
    seriefac=models.CharField(max_length=4)
    numefac=models.IntegerField()
    fechafac=models.DateField()
    discripcion=models.CharField(max_length=250)
    numini=models.IntegerField()
    numfin=models.IntegerField()
    cantidad=models.IntegerField()
    preciouni=models.IntegerField()
    total=models.IntegerField()
    pagada=models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Factura, self).save()

    class Meta:
        verbose_name_plural = "Facturas"