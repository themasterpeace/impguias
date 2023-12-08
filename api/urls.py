from django.urls import path, include
from .views import Clientelist, ClienteDetalle, Provelist


urlpatterns=[
    path('v1/cliente/', Clientelist.as_view(), name='cliente_list'),
    path('v1/cliente/<str:codigo>', ClienteDetalle.as_view(), name='cliente_det'),

    path('v1/porvee/', Provelist.as_view(), name='porvee_list'),
] 