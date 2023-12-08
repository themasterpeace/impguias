from django import forms

from .models import *

class ProveForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields ='__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class FacForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

