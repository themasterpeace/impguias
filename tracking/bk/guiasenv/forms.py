from django import forms
from django.forms import widgets
from .models import *

class GuiaForm(forms.ModelForm):
    class Meta:
        model = GuiasEnv
        fields = [
            'id', 'fecha', 'codigo',
            'cliente', 'tipo_envio','numini',
            'numfin', 'totenvio', 'fpago', 'entregado'
        ]

        labels = {
            'fecha':'Fecha','codigo':'Codigo','cliente':'Cliente',
            'tipo_envio':'Tipo Envio', 'numini':'Numero Inicial',
            'numfin':'Numero Final','totenvio':'Total Enviado',
            'fpago':'Forma Pago', 'entregado':'Entregado'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
