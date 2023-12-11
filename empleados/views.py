from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from openpyxl.styles import Alignment,Border,Font,PatternFill,Side
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse, JsonResponse

from bases.views import SinPrivilegios, ClaseModelo, BaseUpdate, BaseCreate, BaseView
from .models import *
from .forms import *

class NacionalidadView(BaseView):
    permission_required = "empleados.view_nacionalidad"
    model = Nacionalidad
    template_name = "empleados/naclist.html"
    
    def post(self, request, *args, **kwargs):
        data = []
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Nacionalidad.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class NacionalidadNew(BaseCreate):
    permission_required = "empleados.create_nacionalidad"
    model = Nacionalidad
    template_name = "empleados/nacnew.html"
    form_class = NacForm
    success_url = reverse_lazy("empleados:nacionalidad")
    success_message="NACIONALIDAD AGREGADA CORRECTAMENTE"
    

#################Vistas para ingresar el tipo de sexo o genero#########
class SexoView(BaseView):
    permission_required = "empleados.view_sexo"
    model = Sexo
    template_name = "empleados/sexolist.html"

    def post(self, request, *args, **kwargs):
        data = []
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Sexo.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class SexoNew(BaseCreate):
    permission_required = "empleados.create_sexo"
    model = Sexo
    template_name = "empleados/sexonew.html"
    form_class = SexoForm
    success_url = reverse_lazy("empleados:sexolist")
    success_message= "TIPO DE SEXO AGREGADO CORRECTAMENTE"

##################Vistas de estado civil del empleado################

class EstadoCivilView(BaseView):
    permission_required = "empleados.view_estadocivil"
    model = EstadoCivil
    template_name = "empleados/civillist.html"

    def post(self, request, *args, **kwargs):
        data = []
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in EstadoCivil.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class EstadoCivilNew(BaseCreate):
    permission_required = "empleados.create_estadocivil"
    model = EstadoCivil
    template_name = "empleados/civilnew.html"
    form_class = EstadoVicilForm
    success_url = reverse_lazy("empleados:civillist")
    success_message="ESTADO CIVIL AGREGADO CORRECTAMENTE"

 ########################vISTAS TIPO SALARIOS########################

class SalarioView(BaseView):
    permission_required = "empleados.view_tiposalario"
    model = TipoSalario
    template_name = "empleados/salariolist.html"

    def post(self, request, *args, **kwargs):
        data = []
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in TipoSalario.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class SalarioNew(BaseCreate):
    permission_required = "empleados.create_tiposalario"
    model = TipoSalario
    template_name = "empleados/salarionew.html"
    form_class = SalarioForm
    success_url = reverse_lazy("empleados:salariolist")
    success_message="TIPO DE SALARIO AGREGADO CORRECTAMENTE"

######################Vistas de Gerencia############################

class GerenciaView(BaseView):
    permission_required = "empleados.view_gerencia"
    model = Gerencia
    template_name = "empleados/gerencialist.html"
    
    def post(self, request, *args, **kwargs):
        data = []
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Gerencia.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class GerenciaNew(BaseCreate):
    permission_required = "empleados.create_gerencia"
    model = Gerencia
    template_name = "empleados/gerencianew.html"
    form_class = GerenciaForm
    success_url = reverse_lazy("empleados:gerencialist")
    success_message="TIPO DE GERENCIA AGREGADA CORRECTAMENTE"

#################Seccion de vistas para departamentos#############

class DepartamentoView(BaseView):
    permission_required = "empleados.view_departamento"
    model = Departamento
    template_name = "empleados/deptolist.html"
    
    def post(self, request, *args, **kwargs):
        data = []
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Departamento.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class DepartamentoNew(BaseCreate):
    permission_required = "empleados.create_departamento"
    model = Departamento
    template_name = "empleados/deptonew.html"
    form_class = DeptoForm
    success_url = reverse_lazy("empleados:deptolist")
    success_message="DEPARTAMENTO AGREGADO CORRECTAMENTE"

##################Vistar de Puestos#################################

class PuestoView(BaseView):
    permission_required = "empleados.view_puesto"
    model = Puesto
    template_name = "empleados/puestolist.html"
    
    def post(self, request, *args, **kwargs):
        data = []
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Puesto.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class PuestoNew(BaseCreate):
    permission_required = "empleados.create_puesto"
    model = Puesto
    template_name = "empleados/puestonew.html"
    form_class = PuestoForm
    success_url = reverse_lazy("empleados:puestolist")
    success_message="PUESTO AGREGADO EXITOSAMENTE"

##########################Vistas de Sucursal#########################

class SucursalView(BaseView):
    permission_required = "empleados.view_sucursal"
    model = Sucursal
    template_name = "empleados/suclist.html"
    
    def post(self, request, *args, **kwargs):
        data = []
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Sucursal.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class SucursalNew(BaseCreate):
    permission_required = "empleados.create_sucursal"
    model = Sucursal
    template_name = "empleados/sucnew.html"
    form_class = SucursalForm
    success_url = reverse_lazy("empleados:suclist")
    success_message="SUCURSAL AGREGADA CORRECTAMENTE"

####################Vista para Empleados##############################

class EmpleadoView(BaseView):
    permission_required = "empleados.view_empleado"
    model = Empleado
    template_name = "empleados/empleadolist.html"
    
    def post(self, request, *args, **kwargs):
        data = []
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Empleado.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class EmpleadoNew(BaseCreate):
    permission_required = "empleados.create_empleado"
    model = Empleado
    template_name = "empleados/empleadonew.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy("empleados:nominanew")
    success_message="NUEVO EMPLEADO AGREGADO EXITOSAMENTE"

class EmpleadoEdit(BaseUpdate):
    permission_required = "empleados.create_empleado"
    model = Empleado
    template_name = "empleados/empleadonew.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy("empleados:empleadolist")
    success_message="LOS DATOS DEL EMPLEADO SELECCIONADO SE HAN ACTUALIZADO CORRECTAMENTE"

###################Vista de Datos Para Nomina########################

class DanosNominaView(BaseView):
    permission_required = "empleados.view_datosnomina"
    model = DatosNomina
    template_name = "empleados/nomimalist.html"
    
    def post(self, request, *args, **kwargs):
        data = []
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Empleado.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class DanosNominaNew(BaseCreate):
    permission_required = "empleados.create_datosnomina"
    model = DatosNomina
    template_name = "empleados/nominanew.html"
    form_class = DatosNominaForm
    success_url = reverse_lazy("empleados:papelerianew")
    success_message="DATOS DE NOMINA GENERADOS CORRECTAMENTE"

class DanosNominaEdit(BaseUpdate):
    permission_required = "empleados.create_datosnomina"
    model = DatosNomina
    template_name = "empleados/nomimanew.html"
    form_class = DatosNominaForm
    success_url = reverse_lazy("empleados:empleadolist")
    success_message="DATOS DE NOMINA ACTUALIZADOS CORRECTAMENTE"

##########################Datos de vistas de papeleria##################

class PapeleriaView(BaseView):
    permission_required = "empleados.view_papeleria"
    model = Papeleria
    template_name = "empleados/papelerialist.html"
    
    def post(self, request, *args, **kwargs):
        data = []
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Empleado.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class PapeleriaNew(BaseCreate):
    permission_required = "empleados.create_papeleria"
    model = Papeleria
    template_name = "empleados/papelerianew.html"
    form_class = PapeleriaForm
    success_url = reverse_lazy("empleados:empleadolist")
    success_message="PAPELERIA RECIBIDA REGISTRADA CORRECTAMENTE"

class PapeleriaEdit(BaseUpdate):
    permission_required = "empleados.create_papeleria"
    model = Papeleria
    template_name = "empleados/papelerianew.html"
    form_class = PapeleriaForm
    success_url = reverse_lazy("empleados:empleadolist")
    success_message="PAPELERIA RECIBIDA ACTUALIZADA CORRECTAMENTE"