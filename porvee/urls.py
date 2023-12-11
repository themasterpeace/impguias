from django.urls import path

from porvee.views import *

app_name = "porvee"

urlpatterns = [
    path('porvee/list', ProveView.as_view(), name="listprove"),
    path('porvee/new', ProveNew.as_view(), name="newprove"),
    path('porvee/edit/<int:pk>', ProveEdit.as_view(), name="editprove"),

    ###urls facturas###
    path('porvee/list', FacView.as_view(), name="listfac"),
    path('porvee/new', FacNew.as_view(), name="newfac"),
    path('porvee/edit/<int:pk>', FacEdit.as_view(), name="editfac"),

]