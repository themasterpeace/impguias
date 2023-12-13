from django.urls import path
from .views import *

app_name='impa'
urlpatterns = [
    path('imp/list', impview.as_view(), name="listimp"),
    path('imp/new', impnew.as_view(), name="newimp"),
    path('imp/edit<int:pk>', impedit.as_view(), name="editimp"),
    #path('imp/estado/<int:id>', impinactivar, name="imp_inactivar"),
]