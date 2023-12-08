from django.urls import path
from .views import ListarDatosDBFView

urlpatterns = [
    # Otras rutas...
    path('verdatos/', ListarDatosDBFView.as_view(), name='verdatos'),
]
