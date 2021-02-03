from django.db import models
import uuid
from django.utils.html import mark_safe
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Representante(models.Model):
	cedula= models.CharField(max_length=10,null=True)
	nombre=models.CharField(max_length=250) 
	apellido=models.CharField(max_length=250)

	def __str__(self):
		return '%s %s' % (self.nombre, self.apellido)

class Representado(models.Model):
	codigo_qr= models.CharField(max_length=50,primary_key=True, null=False, default="")
	nombre=models.CharField(max_length=250) 
	apellido=models.CharField(max_length=250)
	edad= models.IntegerField()
	

	def __str__(self):
		return '%s %s' % (self.nombre, self.apellido)


class Photo(models.Model):
    file = models.ImageField(upload_to='(%Y_%m_%d)/', null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    observacion= models.TextField(default="", blank=True, null=True)
    periodo = models.CharField(max_length=25, default="")
    representante = models.ForeignKey(Representante, default="",on_delete=models.CASCADE)
    representado = models.ForeignKey(Representado, default="",on_delete=models.CASCADE)
    revisado = models.BooleanField(default=False, null=True)
    CHOICES = [(i,i) for i in range(11)]
    proteinas = models.IntegerField(choices=CHOICES,default=0,blank= True, null=True)
    vegetales = models.IntegerField(choices=CHOICES,default=0,blank= True, null=True)
    carbohidratos = models.IntegerField(choices=CHOICES,default=0,blank= True, null=True)
    puntuacion_general= models.IntegerField(choices=CHOICES,default=0,blank= True, null=True)

    def puntuacion(self):
    	punt= (self.proteinas+self.vegetales+self.carbohidratos)/3
    	self.puntuacion_general= punt
    	return "{0:.2f}".format(self.puntuacion_general)
    
    def image_display(self):
        if self.file:
            return mark_safe('<img src="{}" width="65%" />'.format(self.file.url))
        return ""
    image_display.short_description= 'Imagen'
    
    def __str__(self):
    	return 'Foto %s %s %s' % (self.periodo, self.representado.nombre, self.representado.apellido)

    class Meta:
    	unique_together = ('periodo','representado',)

class Relacion(models.Model):
	representante = models.ForeignKey(Representante, default="", blank=True, on_delete=models.CASCADE)
	representado = models.ForeignKey(Representado, default="",blank=True, on_delete=models.CASCADE)

	class Meta:
	   	unique_together = ('representante','representado',)
	