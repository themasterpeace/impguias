from django import forms

from .models import ImpHija

class HijaForm(forms.ModelForm):
    class Meta:
        model = ImpHija
        fields = [
            'madre', 'pieza','de', 'origen', 'destino'
        ]

        labels = {
            'madre':'Guia Madre', 'pieza':'Pieza', 'de':'De',
            'origen':'Origen','destino':'Destino'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
