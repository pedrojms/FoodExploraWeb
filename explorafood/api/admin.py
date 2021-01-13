from django.contrib import admin
from api.models import *

# Register your models here.
#admin.site.register(Photo)
#admin.site.register(Cliente)

class PhotoAdmin(admin.ModelAdmin):
	list_display = ('id','file', 'createdAt', 'periodo', 'get_name')
	list_filter = ('periodo','createdAt','id_cliente__nombre')
	def get_name(self, obj):
		return obj.id_cliente.nombre+' '+obj.id_cliente.apellido
	get_name.admin_order_field  = 'id_cliente'
	get_name.short_description = 'Cliente Nombre'

class AnalisisAdmin(admin.ModelAdmin):
	list_display = ('id','resultado','observacion','get_photoimage', 'get_photoperiodo' ,'get_photonombre','revisado')
	list_filter= ('id_photo__createdAt', 'revisado')
	def get_photoimage(self, obj):
		return obj.id_photo.file
	def get_photoperiodo(self, obj):
		return obj.id_photo.periodo
	def get_photonombre(self, obj):
		return obj.id_photo.id_cliente.nombre
	get_photoperiodo.admin_order_field  = 'id_photo'
	get_photonombre.admin_order_field  = 'id_photo'
	get_photoimage.short_description = 'Photo File'
	get_photoperiodo.short_description = 'Photo Periodo'
	get_photonombre.short_description = 'Cliente Nombre'


class ClienteAdmin(admin.ModelAdmin):
	list_display = ('cedula','nombre','apellido')

admin.site.register(Photo,PhotoAdmin)
admin.site.register(Analisis, AnalisisAdmin)
admin.site.register(Cliente,ClienteAdmin)