from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.http.response import HttpResponse, JsonResponse
from .models import Proveedor
from bases.views import BaseView, BaseCreate, BaseUpdate
from .forms import *
# Create your views here.

class ProveView(BaseView):
    permission_required = "porvee.view_prove"
    model = Proveedor
    template_name = "porvee/listprove.html"
    
    def post(self, request, *args, **kwargs):
        data = []
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Proveedor.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

class ProveNew(BaseCreate):
    permission_required = "porvee.add_proveedor"
    model = Proveedor
    template_name = "porvee/newprove.html"
    form_class = ProveForm
    success_url = reverse_lazy("porvee:listprove")
    success_message = "PROVEEDOR AGREGADO CORRECTAMENTE"

class ProveEdit(BaseUpdate):
    permission_required = "porvee.update_proveedor"
    model = Proveedor
    template_name = "porvee/newprove.html"
    form_class = ProveForm
    success_url = reverse_lazy("porvee:listprove")
    success_message = "PROVEEDOR ACTUALIZADO CORRECTAMENTE"
 