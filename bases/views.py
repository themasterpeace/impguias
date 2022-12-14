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
from .forms import *
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
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['panel']= 'Panel de Administracion'
        context['grafico'] = self.get_graph_sales_year_month()
        return context
  

class HomeSinPrivilegios(LoginRequiredMixin, TemplateView):
    login_url = "bases:login"
    template_name="bases/sin_privilegios.html"

