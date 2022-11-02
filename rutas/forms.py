from django import forms

from .models import Ruta

class RutaForm(forms.ModelForm):
    class Meta:
        model = Ruta
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })