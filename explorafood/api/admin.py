from django.contrib import admin
from django.http import HttpResponseRedirect
from api.models import *
from django.contrib import messages

# Register your models here.
#admin.site.register(Photo)
#admin.site.register(Cliente)

admin.site.site_header = "Administración Food Explora"

class PhotoAdmin(admin.ModelAdmin):
	change_form_template = 'admin/api/photo/move_button.html'
	readonly_fields = ['puntuacion','image_display','createdAt','periodo','representante','representado']
	#fields= ('image_display','observacion','createdAt','periodo','representante','representado','revisado')
	fieldsets = (
        ('Evaluacion', {
            'fields': ('image_display', 'observacion')
        }),
        ('Puntuacion',{
        	'fields':(('proteinas','vegetales','carbohidratos'),'puntuacion')
        }),
        ('Datos', {
            'fields': ('periodo','createdAt','representado', 'representante')
        }),
        ('Revision', {
            'fields': ['revisado']
        }),

    )
	list_display = ('id','revisado','image_display', 'createdAt', 'periodo', 'get_name','get_representado')
	list_filter = ('periodo','createdAt','revisado')
	def get_name(self, obj):
		return obj.representante.nombre+' '+obj.representante.apellido
	get_name.admin_order_field  = 'representante'
	get_name.short_description = 'Representante'
	def get_representado(self, obj):
		return obj.representado.nombre+' '+obj.representado.apellido
	get_representado.admin_order_field  = 'representante'
	get_representado.short_description = 'Representado'
	

	def response_change(self, request, obj):
		if "siguiente" in request.POST:
			try:
				sig=Photo.objects.get(id=obj.id+1)
				while sig.revisado:
					sig=Photo.objects.get(id=sig.id+1)
				return HttpResponseRedirect("../../%s/" % sig.id)
			except:

				messages.error(request, 'No existe imagen siguiente')
				return HttpResponseRedirect(".")

		if "anterior" in request.POST:
			try:
				ant=Photo.objects.get(id=obj.id-1)
				while ant.revisado:
					ant=Photo.objects.get(id=ant.id-1)
				return HttpResponseRedirect("../../%s/" % ant.id)
			except:

				messages.error(request,'No existe imagen anterior')
				return HttpResponseRedirect(".")
		return super().response_change(request, obj)



class RepresentanteAdmin(admin.ModelAdmin):
	list_display = ('cedula','nombre','apellido')

class RelacionAdmin(admin.ModelAdmin):
	list_display= ('id','get_representante','get_representado')
	def get_representante(self, obj):
		return obj.representante.nombre+' '+obj.representante.apellido
	get_representante.admin_order_field  = 'representante'
	get_representante.short_description = 'Representante'
	def get_representado(self, obj):
		return obj.representado.nombre+' '+obj.representado.apellido
	get_representado.admin_order_field  = 'representante'
	get_representado.short_description = 'Representado'


admin.site.register(Photo,PhotoAdmin)
admin.site.register(Representado)
admin.site.register(Representante,RepresentanteAdmin)
admin.site.register(Relacion,RelacionAdmin)