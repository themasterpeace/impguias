from django.shortcuts import render

from rest_framework.views import APIView	
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from. serializers import *
from guiasenv.models import Cliente
from porvee.models import Proveedor

from django.db.models import Q 

class Clientelist(APIView):
    def get(self,request):
        clie = Cliente.objects.all()
        data = ClienteSerializer(clie,many=True).data
        return Response(data)

class ClienteDetalle(APIView):
    def get(self, request, codigo):
        clie = get_object_or_404(Cliente, Q (codigo=codigo))  # Obtén el objeto Cliente desde la base de datos
        serializer = ClienteSerializer(clie)  # Crea una instancia del serializer
        data = serializer.data # Serializa el objeto Cliente en un diccionario de datos
        return Response(data)
    
class Provelist(APIView):
    def get(self,request):
        prov = Proveedor.objects.all()
        data = ProveSerializer(prov,many=True).data
        return Response(data)