import imp
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from datetime import date
from collections import Counter
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from guiasenv.models import GuiasEnv


def Dashborad(request):
    template = "bases/home.html"

    #-------------tipo envio------------------#
    tp_cte = GuiasEnv.objects.filter(tipo_envio='CONTRA ENTREGA').count()
    tp_cte = int(tp_cte)
    print('Cantidad de veces enviando contraentrega',tp_cte)

    tp_mani = GuiasEnv.objects.filter(tipo_envio='MANIFIESTOS').count()
    tp_mani = int(tp_mani)
    print('Cantidad de veces enviando manifiestos',tp_mani)

    tp_gm = GuiasEnv.objects.filter(tipo_envio='GUIA MADRE').count()
    tp_gm = int(tp_gm)
    print('Cantidad de veces enviando guias madre',tp_gm)

    tp_GH = GuiasEnv.objects.filter(tipo_envio='GUIA HIJA').count()
    tp_GH = int(tp_GH)
    print('Cantidad de veces enviando guias hija',tp_GH)

    #-------------------Fora de Pago-----------------------#
    fp_xco = GuiasEnv.objects.filter(fp_xco='POR COBRAR').count()
    fp_xco = int(fp_xco)
    print('Cantidad de veces imprimiendo guias Por Cobrar',fp_xco)

    fp_cre = GuiasEnv.objects.filter(fp_xco='CREDITO').count()
    fp_cre = int(fp_cre)
    print('Cantidad de veces imprimiendo guias credito',fp_cre)

    tipoenvio_list = ['CONTRA ENTREGA', 'MANIFIESTOS', 'GUIA MADRE', 'GUIA HIJA']
    tipoenvio_number = [tp_cte,tp_GH,tp_gm, tp_mani]

    fpago_list = ['POR COBRAR', ' CREDITO']
    fpago_number = [fp_xco, fp_cre]
    contexto = {'tipoenvio_list':tipoenvio_list, 'tipoenvio_number':tipoenvio_number, 'fpago_list':fpago_list, 'fpago_number':fpago_number}
    
    return render(request, template, contexto)

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


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url='bases:login'
  

class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = "bases:login"
    template_name="bases/sin_privilegios.html"


