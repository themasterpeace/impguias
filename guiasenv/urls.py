from django.urls import path
from django.contrib.auth import views as auth_views

from guiasenv.views import *

urlpatterns = [
    path('guia/list', GuiaView.as_view(), name="guialist"),
    path('guia/new', GuiasNew.as_view(), name="guianew"),
    path('guia/edit<int:pk>', GuiaEdit.as_view(), name="guiaedit"),
]