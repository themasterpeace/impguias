from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import GuiaForm



class GuiaView(LoginRequiredMixin, generic.ListView):
    model = GuiasEnv
    template_name = "guiasenv/guialist.html"
    context_object_name = "obj"
    login_url = "bases:login"


class GuiaNew(LoginRequiredMixin, generic.CreateView):
    model = GuiasEnv
    template_name = "guiasenv/guianew.html"
    context_object_name = "obj"
    form_class = GuiaForm
    succes_url = reverse_lazy("guiasenv:guialist")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)


class GuiaEdit(generic.UpdateView):
    model = GuiasEnv
    template_name="guiasenv/guianew.html"
    context_object_name="obj"
    form_class = GuiaForm
    success_url=reverse_lazy("guiasenv:guialist")
    login_url = "bases:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)