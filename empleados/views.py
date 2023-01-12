from django.shortcuts import render, redirect
from django.views.generic import  ListView, CreateView, UpdateView, TemplateView
from django.contrib import messages
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
from openpyxl import Workbook
from openpyxl.styles import Alignment,Border,Font,PatternFill,Side
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponse, JsonResponse

from bases.views import SinPrivilegios, ClaseModelo
from .models import *
from .forms import *

class NacionalidadView(SinPrivilegios, ListView):
    permission_required = "empleados.view_nacionalidad"
    model = Nacionalidad
    template_name = "empleados/naclist.html"
    context_object_name = "obj"
    login_url = "bases:login"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
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

class NacionalidadNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "empleados.create_nacionalidad"
    model = Nacionalidad
    template_name = "empleados/nacnew.html"
    context_object_name = "obj"
    form_class = NacForm
    success_url = reverse_lazy("empleados:nacionalidad")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

#################Vistas para ingresar el tipo de sexo o genero#########
class SexoView(SinPrivilegios, ListView):
    permission_required = "empleados.view_sexo"
    model = Sexo
    template_name = "empleados/sexolist.html"
    context_object_name = "obj"
    login_url = "bases:login"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
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

class SexoNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "empleados.create_sexo"
    model = Sexo
    template_name = "empleados/sexonew.html"
    context_object_name = "obj"
    form_class = SexoForm
    success_url = reverse_lazy("empleados:sexolist")
    login_url = "bases:login" 

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

##################Vistas de estado civil del empleado################

class EstadoCivilView(SinPrivilegios, ListView):
    permission_required = "empleados.view_estadocivil"
    model = EstadoCivil
    template_name = "empleados/civillist.html"
    context_object_name = "obj"
    login_url = "bases:login"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
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

class EstadoCivilNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "empleados.create_estadocivil"
    model = EstadoCivil
    template_name = "empleados/civilnew.html"
    context_object_name = "obj"
    form_class = EstadoVicilForm
    success_url = reverse_lazy("empleados:civillist")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

 ########################vISTAS TIPO SALARIOS########################

class SalarioView(SinPrivilegios, ListView):
    permission_required = "empleados.view_tiposalario"
    model = TipoSalario
    template_name = "empleados/salariolist.html"
    context_object_name = "obj"
    login_url = "bases:login"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
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

class SalarioNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "empleados.create_tiposalario"
    model = TipoSalario
    template_name = "empleados/salarionew.html"
    context_object_name = "obj"
    form_class = SalarioForm
    success_url = reverse_lazy("empleados:salariolist")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

######################Vistas de Gerencia############################

class GerenciaView(SinPrivilegios, ListView):
    permission_required = "empleados.view_gerencia"
    model = Gerencia
    template_name = "empleados/gerencialist.html"
    context_object_name = "obj"
    login_url = "bases:login"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
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

class GerenciaNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "empleados.create_gerencia"
    model = Gerencia
    template_name = "empleados/gerencianew.html"
    context_object_name = "obj"
    form_class = GerenciaForm
    success_url = reverse_lazy("empleados:gerencialist")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

#################Seccion de vistas para departamentos#############

class DepartamentoView(SinPrivilegios, ListView):
    permission_required = "empleados.view_departamento"
    model = Departamento
    template_name = "empleados/deptolist.html"
    context_object_name = "obj"
    login_url = "bases:login"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
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

class DepartamentoNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "empleados.create_departamento"
    model = Departamento
    template_name = "empleados/deptonew.html"
    context_object_name = "obj"
    form_class = DeptoForm
    success_url = reverse_lazy("empleados:deptolist")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

##################Vistar de Puestos#################################

class PuestoView(SinPrivilegios, ListView):
    permission_required = "empleados.view_puesto"
    model = Puesto
    template_name = "empleados/puestolist.html"
    context_object_name = "obj"
    login_url = "bases:login"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
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

class PuestoNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "empleados.create_puesto"
    model = Puesto
    template_name = "empleados/puestonew.html"
    context_object_name = "obj"
    form_class = PuestoForm
    success_url = reverse_lazy("empleados:puestolist")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

##########################Vistas de Sucursal#########################

class SucursalView(SinPrivilegios, ListView):
    permission_required = "empleados.view_sucursal"
    model = Sucursal
    template_name = "empleados/suclist.html"
    context_object_name = "obj"
    login_url = "bases:login"

class SucursalNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "empleados.create_sucursal"
    model = Sucursal
    template_name = "empleados/sucnew.html"
    context_object_name = "obj"
    form_class = SucursalForm
    success_url = reverse_lazy("empleados:suclist")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

####################Vista para Empleados##############################

class EmpleadoView(SinPrivilegios, ListView):
    permission_required = "empleados.view_empleado"
    model = Empleado
    template_name = "empleados/empleadolist.html"
    context_object_name = "obj"
    login_url = "bases:login"

class EmpleadoNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "empleados.create_empleado"
    model = Empleado
    template_name = "empleados/empleadonew.html"
    context_object_name = "obj"
    form_class = EmpleadoForm
    success_url = reverse_lazy("empleados:nominanew")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class EmpleadoEdit(SuccessMessageMixin, SinPrivilegios, UpdateView):
    permission_required = "empleados.create_empleado"
    model = Empleado
    template_name = "empleados/empleadonew.html"
    context_object_name = "obj"
    form_class = EmpleadoForm
    success_url = reverse_lazy("empleados:empleadolist")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)

###################Vista de Datos Para Nomina########################

class DanosNominaView(SinPrivilegios, ListView):
    permission_required = "empleados.view_datosnomina"
    model = DatosNomina
    template_name = "empleados/nomimalist.html"
    context_object_name = "obj"
    login_url = "bases:login"

class DanosNominaNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "empleados.create_datosnomina"
    model = DatosNomina
    template_name = "empleados/nomimanew.html"
    context_object_name = "obj"
    form_class = DatosNominaForm
    success_url = reverse_lazy("empleados:papelerianew")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class DanosNominaEdit(SuccessMessageMixin, SinPrivilegios, UpdateView):
    permission_required = "empleados.create_datosnomina"
    model = DatosNomina
    template_name = "empleados/nomimanew.html"
    context_object_name = "obj"
    form_class = DatosNominaForm
    success_url = reverse_lazy("empleados:empleadolist")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)

##########################Datos de vistas de papeleria##################

class PapeleriaView(SinPrivilegios, ListView):
    permission_required = "empleados.view_papeleria"
    model = Papeleria
    template_name = "empleados/papelerialist.html"
    context_object_name = "obj"
    login_url = "bases:login"

class PapeleriaNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "empleados.create_papeleria"
    model = Papeleria
    template_name = "empleados/papelerianew.html"
    context_object_name = "obj"
    form_class = PapeleriaForm
    success_url = reverse_lazy("empleados:empleadolist")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class PapeleriaEdit(SuccessMessageMixin, SinPrivilegios, UpdateView):
    permission_required = "empleados.create_papeleria"
    model = Papeleria
    template_name = "empleados/papelerianew.html"
    context_object_name = "obj"
    form_class = PapeleriaForm
    success_url = reverse_lazy("empleados:empleadolist")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)