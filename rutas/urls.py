from django.urls import path

from rutas.views import RutaView, RutaNew, RutaEdit

app_name = "rutas"

urlpatterns = [
    path('ruta/list', RutaView.as_view(), name="list_ruta"),
    path('ruta/new', RutaNew.as_view(), name="new_ruta"),
    path('ruta/edit/<int:pk>', RutaEdit.as_view(), name="edit_ruta"),
]
