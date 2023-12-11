from dataclasses import field
from pyexpat import model
from rest_framework import serializers


from guiasenv.models import *
from porvee.models import Proveedor

class ClienteSerializer(serializers.ModelSerializer):
    nombre = serializers.StringRelatedField()
    formapago = serializers.StringRelatedField()
    
    class Meta:
        model = Cliente
        fields = '__all__'

class ProveSerializer(serializers.ModelSerializer):
    nombre = serializers.StringRelatedField()
    direccion = serializers.StringRelatedField()

    class Meta:
        model = Proveedor
        fields = '__all__'

