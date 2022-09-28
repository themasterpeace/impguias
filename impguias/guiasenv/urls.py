from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from guiasenv.views import *

app_name = "guiasenv"

urlpatterns = [
    re_path('guia/list', GuiaView.as_view(), name="guialist"),
    path('guia/new', GuiaNew.as_view(), name="guianew"),
    path('guia/edit/<int:pk>', GuiaEdit.as_view(), name="guiaedit"),
    path('guia/entregado/<int:id>', entregado, name="entregado"),

    path('guia/excel', ReporteClienteExcel.as_view(), name="guiaexcel"),
]