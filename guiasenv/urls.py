from django.urls import path, re_path
from django.contrib.auth import views as auth_views

from guiasenv.views import *

urlpatterns = [
    re_path(r'^guia/(?P<slug>[-\w]+)/$', GuiaView.as_view(), name="guialist"),
    path('guia/new', GuiasNew.as_view(), name="guianew"),
    path('guia/edit<int:pk>', GuiaEdit.as_view(), name="guiaedit"),
]