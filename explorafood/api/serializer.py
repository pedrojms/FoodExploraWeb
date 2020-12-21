from django.shortcuts import render
from rest_framework import serializers
from . import models

# Create your views here.
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = '__all__'