from django.db import models
import uuid

# Create your models here.

class Cliente(models.Model):
	codigo_qr= models.CharField(max_length=50, null=True, blank=True)
	cedula= models.CharField(max_length=10,null=True)
	nombre=models.CharField(max_length=250) 
	apellido=models.CharField(max_length=250)

	'''def __str__(self):
		return '%s %s' % (self.nombre, self.apellido)'''

class Photo(models.Model):
    file = models.ImageField(upload_to='(%Y_%m_%d)/', null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    periodo = models.CharField(max_length=25, default="")
    id_cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)

class Analisis(models.Model):
	resultado= models.CharField(max_length=100, null=True)
	observacion= models.CharField(max_length=10000, null=True)
	id_photo= models.ForeignKey(Photo,null=True, blank=True, on_delete=models.CASCADE)
	revisado = models.BooleanField()