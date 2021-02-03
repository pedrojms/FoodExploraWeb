from django.shortcuts import render
from rest_framework import serializers
from . import models
from api.models import Representado

# Create your views here.
class PhotoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = '__all__'

class RepresentanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Representante
        fields = '__all__'

class RepresentadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Representado
        fields = '__all__'

class RelacionSerializer(serializers.ModelSerializer):
	
	representado=RepresentadoSerializer(read_only=True)
	representadoid= serializers.PrimaryKeyRelatedField(write_only=True, queryset=Representado.objects.all(), source='representado')

	class Meta:
		model = models.Relacion
		fields = ('representado','representadoid','representante')