from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from guiasenv.views import *

app_name = "guiasenv"

urlpatterns = [
    re_path('guia/list', GuiaView.as_view(), name="guialist"),
    path('guia/new', GuiaNew.as_view(), name="guianew"),
    path('guia/edit/<int:pk>', GuiaEdit.as_view(), name="guiaedit"),
    path('guia/entregado/<int:id>', entregado, name="entregado"),

    path('cliente/list', ClienteListView.as_view(), name="clientelist"),
    path('cliente/new', ClienteNew.as_view(), name="clientenew"),
    path('cliente/edit/<int:pk>', ClienteEdit.as_view(), name="clienteedit"),
    #path('cliente/entregado/<int:id>', entregado, name="entregado"),

    path('guia/reporte', Reportes.as_view(), name="reporte"),
    path('guia/excel', ReporteClienteExcel.as_view(), name="guiaexcel"),
    path('guia/excelgen', ReporteGeneralExcel.as_view(), name="guiaexcelgen"),
    path('guia/excelfech', ReporteFechaExcel.as_view(), name="guiaexcelfech"),
]