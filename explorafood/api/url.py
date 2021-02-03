from django.urls import path,include
from django.conf.urls import url
from rest_framework import routers
from . import views
from api.views import *

router= routers.DefaultRouter()
router.register('photo',PhotoUploadView,'photo')
router.register('representante',RepresentanteViewset,'representante')
router.register('representado',RepresentadoViewset,'representado')
router.register('relacion',RelacionViewset,'relacion')


urlpatterns = [
	url(r'^', include(router.urls)),

   ]