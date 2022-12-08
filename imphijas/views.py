from django.shortcuts import render, redirect

from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.contrib import messages
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse, JsonResponse

from bases.views import SinPrivilegios
from .models import ImpHija
from .forms import HijaForm

class HijaView(SinPrivilegios, ListView):
    permission_required = "imphijas.view_imphija"
    model = ImpHija
    template_name = "imphijas/hijaslist.html"
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
                for i in ImpHija.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class HijaNew(SuccessMessageMixin, SinPrivilegios, CreateView):
    permission_required = "imphijas.create_imphija"
    model = ImpHija
    template_name = "imphijas/hijasnew.html"
    context_object_name = "obj"
    form_class = HijaForm
    success_url = reverse_lazy("imphijas:hijalist")
    success_message = "IMPRESION DE GUIAS EXITOSA"
    login_url = "bases:login"



