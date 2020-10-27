
from rest_framework import serializers
from django.contrib.auth import authenticate

class api_correoSerializer(serializers.Serializer):
    
    nombre = serializers.CharField()
    correo = serializers.CharField()
    asunto = serializers.CharField(required=False)
    mensaje = serializers.CharField()

    def create(self,data):
        return data