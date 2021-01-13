from django.urls import path,include
from django.conf.urls import url
from rest_framework import routers
from . import views
from api.views import *

router= routers.DefaultRouter()
router.register('photo',PhotoUploadView,'photo')
router.register('cliente',ClienteViewset,'cliente')


urlpatterns = [
	url(r'^', include(router.urls)),

   ]