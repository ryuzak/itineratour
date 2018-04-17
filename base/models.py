# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone

from django.db import models

from intineratour import utilies as ut
# Create your models here.
#--clase que tiene todos los campos de control utilizados por los demas modelos
#--todos los modelos deben de heredar esta clase
#class BaseModel(models.Model):
class BaseModel(models.Model):   
    status = models.CharField( max_length = 2, choices = ut.STATUS_CHOICES, default = 1 )
    created_date =  models.DateTimeField( default = timezone.now)
    last_modified_date = models.DateTimeField( null = True )
    deleted_date = models.DateTimeField( null = True, default = timezone.now)
    createdby_id = models.IntegerField( default = 0 )
    modifiedby_id = models.IntegerField( default = 0 )

    #campo de sincronizacion entre la plataforma y la app movil
    synckey = models.CharField( max_length = 512, default = "" )

    class Meta:
        abstract=True