from django.shortcuts import render
from . import models
from . import serializer
from api.serializer import *
from rest_framework import viewsets
from rest_framework import generics, status, serializers
from rest_framework.views import APIView
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

# Create your views here.
class PhotoUploadView(viewsets.ModelViewSet):
	parser_class = (FileUploadParser,)
	queryset = models.Photo.objects.all()
	serializer_class = serializer.PhotoUploadSerializer
	def post(self, request, format=None):
		print(request.data)
		file_serializer = PhotoUploadSerializer(data=request.data)
		if file_serializer.is_valid():
			file_serializer.save()
			return Response(file_serializer.data, status=status.HTTP_201_CREATED)
		else:
			print(file_serializer.errors)
			return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClienteViewset(viewsets.ModelViewSet):
	queryset = models.Cliente.objects.all()
	serializer_class = serializer.ClienteSerializer

	def post(self, request, format=None):
		# persona=models.Usuario.objects.all().last()
		serializercl = serializer.ClienteSerializer(data=request.data)
		if serializercl.is_valid():
			serializercl.save()
			return Response(serializercl.data, status=status.HTTP_201_CREATED)
		return Response(serializercl.errors, status=status.HTTP_400_BAD_REQUEST)     