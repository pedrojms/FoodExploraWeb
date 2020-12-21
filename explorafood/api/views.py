from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from . import models
from . import serializer

# Create your views here.
class PhotoView(generics.ListAPIView):    
	queryset = models.Photo.objects.all()
	serializer_class = serializer.PhotoSerializer