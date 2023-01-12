from django import forms
from django.forms import widgets

from .models import *


class NacForm(forms.ModelForm):
    class Meta:
        model = Nacionalidad
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
              self.fields[field].widget.attrs.update({
                  'class':'form-control'
              })

class SexoForm(forms.ModelForm):
    class Meta:
        model = Sexo
        fields = '__all__'

        def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          for field in iter(self.fields):
              self.fields[field].widget.attrs.update({
                  'class':'form-control'
              })

class EstadoVicilForm(forms.ModelForm):
    class Meta:
        model = EstadoCivil
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, *kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })

class SalarioForm(forms.ModelForm):
    class Meta:
        model = TipoSalario
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, *kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                'class':'form-control'
            })

class GerenciaForm(forms.ModelForm):
    class Meta:
        model = Gerencia
        fields ='__all__'

        def __init__(self,*args, **kwargs):
            super().__init__(*args,**kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })

class DeptoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = '__all__'

        def __init__(self,*args, **kwargs):
            super().__init__(*args,**kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })

class PuestoForm(forms.ModelForm):
    class Meta:
        model = Puesto
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class':'form-control'
                })
        

class SucursalForm(forms.ModelForm):
    pass

class EmpleadoForm(forms.ModelForm):
    pass

class DatosNominaForm(forms.ModelForm):
    pass

class PapeleriaForm(forms.ModelForm):
    pass

