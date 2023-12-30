import time

from re import  template
from django.http import request 
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import * 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib import messages 
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from guiasenv.views import ClienteListView

from bases.views import SinPrivilegios, BaseCreate

# Create your views here.

class impview(LoginRequiredMixin, ListView):
    model = ImpGuias
    template_name ="impa/listimp.html"
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
                for i in ImpGuias.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)


class impnew(BaseCreate):
    permission_required="impa.create_impguias"
    model = ImpGuias
    template_name = "impa/newimp.html"
    form_class = ImpresionForm
    success_url = reverse_lazy("impa:listimp")
    success_message = "IMPRESION DE GUIAS MADRE ENVIADA EXITOSAMENTE"
    
        
class impedit(LoginRequiredMixin, UpdateView):
    model = ImpGuias
    template_name="impa/newimp.html"
    context_object_name="obj"
    form_class = ImpresionForm
    success_url=reverse_lazy("imp:listimp")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

class impdel(LoginRequiredMixin, DeleteView):
    model = ImpGuias
    template_name='impa/eliminar.html'
    context_object_name='obj'
    success_url=reverse_lazy("impa:listimp")
    login_url = "bases:login"

class buscarcli(ClienteListView):
    template_name='link/buscar_cli.html'

class buscardes(ClienteListView):
    template_name='link/buscar_des.html'

#class buscarprod(tarifarioview):
#    template_name='link/buscar_prod.html'