from audioop import reverse
from re import template
from django.http import request 
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
#from openpyxl import Workbook
#from openpyxl.writer.excel import save_virtual_workbook
# Create your views here.

class GuiasNew(generic.CreateView):
    model = GuiasEnv
    template_name = "guiasenv/guianew.html"
    context_object_name = "obj"
    form_class = GuiaForm
    succes_url = reverse_lazy("guiasenv:guialist")
    
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class GuiaView(generic.ListView):
    model = GuiasEnv
    template_name = "guiasenv/guialist.html"
    context_object_name = "obj"

class GuiaEdit(generic.UpdateView):
    model = GuiasEnv
    template_name="guiasenv/guianew.html"
    context_object_name="obj"
    form_class = GuiaForm
    success_url=reverse_lazy("guiasenv:guialist")
    
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)