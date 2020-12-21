from django.db import models

# Create your models here.
class Photo(models.Model):
    
    file = models.ImageField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    periodo = models.CharField(max_length=250)