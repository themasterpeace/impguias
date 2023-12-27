import re
from django import forms
from django.db.models import fields
from django.forms import CharField, widgets, ValidationError
#from pyparsing import Char
from impa.models import *
from bases.models import ClaseModelo 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ImpresionForm(forms.ModelForm):

    codigo_desti = CharField(required=False)
    destinatario = CharField(required=False)
    dirdes = CharField(required=False)
    teldes = CharField(required=False)
    zonades = CharField(required=False)
    munides = CharField(required=False)
    destino = CharField(required=False)
    rutades = CharField(required=False)
    #codigo = CharField(required=False)
    #cliente = CharField(required=False)

    class Meta:
        model = ImpGuias
        fields = ['fecha','codigo_cliente',
                 'remitente','dirrem','tel','origen',
                 'codigo_desti','destinatario','dirdes','teldes',
                 'zonades','munides','destino','rutades','fpago',
                 'numini','numfin', 'totalimp'
                 ]
        labels={
            'fecha':"Fecha",'codigo_cliente':"Codigo Cliente",
            'remitente':"Remitente",'dirrem':"Direccion Remitente",'tel':"Telefono",'origen':"Origen",
            'codigo_desti':"Codigo Dest",'destinatario':"Destinatario",'dirdes':"Direccion Dest",'teldes':"Telefono",
            'zonades':"Zona",'munides':"Municipio",'destino':"Destino",'rutades':"Ruta",'fpago':"Forma de Pago",
            'numini':"Numero Inicial",'numfin':"Numero Final",'totalimp':"Total Guías A Imprimir"
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            }) 