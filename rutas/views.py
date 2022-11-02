from django.shortcuts import render, redirect

from django.views.generic import  ListView, CreateView, UpdateView, TemplateView
from django.contrib import messages
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.decorators import login_required, permission_required
from django.http.response import HttpResponse, JsonResponse

from bases.views import SinPrivilegios
from .models import Ruta
from .forms import RutaForm
# Create your views here.

class RutaView(SinPrivilegios, ListView):
    permission_required = "rutas.view_ruta"
    model = Ruta
    template_name = "rutas/list_ruta.html"
    context_object_name = "obj"
    login_url = "bases:login"

class RutaNew(SuccessMessageMixin ,SinPrivilegios, CreateView):
    permission_required = "rutas.create_ruta"
    model = Ruta
    template_name = "rutas/new_ruta.html"
    context_object_name = "obj"
    form_class = RutaForm
    success_url = reverse_lazy("rutas:list_ruta")
    success_message = "RUTA AGREGADA CORRECTAMENTE"
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class RutaEdit(SuccessMessageMixin, SinPrivilegios, UpdateView):
    permission_required = "rutas.update_ruta"
    model = Ruta
    template_name = "rutas/new_ruta.html"
    context_object_name = "obj"
    form_class = RutaForm
    success_url = reverse_lazy("rutas:list_ruta")
    success_message = "RUTA ACTUALIZADA CORRECTAMENTE"
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)