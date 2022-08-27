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

class guiasnew(LoginRequiredMixin, generic.CreateView):
    model = GuiasEnv
