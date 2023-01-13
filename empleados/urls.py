from django.urls import path
from django.contrib.auth import views as auth_views

from empleados.views import *

app_name = "empleados"

urlpatterns = [
    ############ urls de nacionalidad ######################
    path('nacionalidad/list', NacionalidadView.as_view(), name='nacionalidad'),
    path('nacionalidad/new', NacionalidadNew.as_view(), name='nacnew'),

    ################urls de sexo#############################
    path('sexo/list', SexoView.as_view(), name='sexolist'),
    path('sexo/new', SexoNew.as_view(), name='sexonew'),

    ################urls de estado civil#############################
    path('civil/list', EstadoCivilView.as_view(), name='civillist'),
    path('civil/new', EstadoCivilNew.as_view(), name='civilnew'),

    ################urls de tipo salario#############################
    path('salario/list', SalarioView.as_view(), name='salariolist'),
    path('salario/new', SalarioNew.as_view(), name='salarionew'),

    ################urls de tipo gerencia#############################
    path('gerencia/list', GerenciaView.as_view(), name='gerencialist'),
    path('gerencia/new', GerenciaNew.as_view(), name='gerencianew'),

    ################urls de departamentos#############################
    path('depto/list', DepartamentoView.as_view(), name='deptolist'),
    path('depto/new', DepartamentoNew.as_view(), name='deptonew'),

    ################urls de puestos#############################
    path('puesto/list', PuestoView.as_view(), name='puestolist'),
    path('puesto/new', PuestoNew.as_view(), name='puestonew'),

    ################urls de Sucursales#############################
    path('sucursal/list', SucursalView.as_view(), name='suclist'),
    path('sucursal/new', SucursalNew.as_view(), name='sucnew'),

    ################urls de Empleados#############################
    path('empleado/list', EmpleadoView.as_view(), name='empleadolist'),
    path('empleado/new', EmpleadoNew.as_view(), name = 'empleadonew'),

    ################urls de Datos Nomina#############################
    path('nomina/list', DanosNominaView.as_view(), name='nominalist'),
    path('nomina/new', DanosNominaNew.as_view(), name='nominanew'),

    ################urls de Papeleria #############################
    path('papeleria/list', PapeleriaView.as_view(), name='papelerialist'),
    path('papeleria/new', PapeleriaNew.as_view(), name='papelerianew'),

    


    

]
