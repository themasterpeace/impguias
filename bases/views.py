import imp
import calendar
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from datetime import date, datetime
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from collections import Counter
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import *
<<<<<<< HEAD
#from .forms import *
=======
from .forms import *
>>>>>>> 1c8954badf90d7b6dbf73074e04cc47f750d8369
from guiasenv.models import GuiasEnv



class MixinFormInvalid:
    def form_invalid(self,form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin, MixinFormInvalid):
    login_url = 'bases:login'
    raise_exception=False
    redirect_field_name="redirecto_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class Home(TemplateView):
    template_name = 'bases/home.html'
<<<<<<< HEAD
=======
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'get_graph_sales_year_month':
                data = {
                    'name':'Porcentaje de Impresiones',
                    'colorByPoint': True,
                    'showInLegend': False,
                    'data': self.get_graph_sales_year_month()
                }
            elif action == 'get_graph_sales_fpago_year':
                data = {
                    'name':'FPAGO',
                    'colorByPoint': True,
                    'showInLegend': False,
                    'data': self.get_graph_sales_fpago_year()
                }
            else:
                data['error'] = 'No existen datos que mostrar'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_graph_sales_year_month(self):
        data = []
        try:
            year = datetime.now().year - 1
            for m in range(1, 13):
                totenvio = GuiasEnv.objects.filter(fecha__year=year, fecha__month=m).aggregate(r=Coalesce(Sum('totenvio'), 0)).get('r')
                data.append(float(totenvio))
        except:
            pass
        return data
        
    def get_graph_sales_fpago_year(self):
        data = []
        try:
            year = datetime.now().year - 1
            for m in range(1, 13):
                fpagos = GuiasEnv.objects.filter(fecha__year=year, fecha__month=m).values('tipo_envio').annotate(total=Sum('totenvio'))
                for fpago in fpagos:
                    data.append({
                        'name': fpago['tipo_envio'],
                        'y': float(fpago['total'])
                    })
        except Exception as e:
            print(e)
            pass
        print(data)
        return data
>>>>>>> 1c8954badf90d7b6dbf73074e04cc47f750d8369

    def get_graph_sales_pastyear_month(self):
        data = []
        try:
            year = datetime.now().year -1
            for m in range(1, 13):
                totenvio = GuiasEnv.objects.filter(fecha__year=year, fecha__month=m).aggregate(r=Coalesce(Sum('totenvio'), 0)).get('r')
                data.append(float(totenvio))
        except:
            pass
        return data
   
    def get_graph_sales_year_month(self):
        data = []
        try:
            year = datetime.now().year
            for m in range(1, 13):
                totenvio = GuiasEnv.objects.filter(fecha__year=year, fecha__month=m).aggregate(r=Coalesce(Sum('totenvio'), 0)).get('r')
                data.append(float(totenvio))
        except:
            pass
        return data

    def get_graph_sales_year_tipoenvio(self):
        data = []
        try:
            year = datetime.now().year
            for tipo_envio in data:
                totenvio = GuiasEnv.objects.filter(fecha__year=year, tipo_envio=tipo_envio).aggregate(r=Coalesce(Sum('totenvio'), 0)).get('r')
                data.append(float(totenvio))
                print(data)
        except:
            pass
        return data
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel']= 'Panel de Administracion'
        context['grafico'] = self.get_graph_sales_year_month()
<<<<<<< HEAD
        context['grafico2'] = self.get_graph_sales_pastyear_month()
        context['grafico3'] = self.get_graph_sales_year_tipoenvio()
=======
        context['grafico1'] = self.get_graph_sales_fpago_year()
>>>>>>> 1c8954badf90d7b6dbf73074e04cc47f750d8369
        return context
  

class HomeSinPrivilegios(LoginRequiredMixin, TemplateView):
    login_url = "bases:login"
<<<<<<< HEAD
    template_name="bases/sin_privilegios.html"
=======
    template_name="bases/sin_privilegios.html"

>>>>>>> 1c8954badf90d7b6dbf73074e04cc47f750d8369
