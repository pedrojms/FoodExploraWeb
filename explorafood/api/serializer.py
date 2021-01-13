from django.shortcuts import render
from rest_framework import serializers
from . import models

# Create your views here.
class PhotoUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cliente
        fields = '__all__'