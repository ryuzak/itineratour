# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from intineratour.settings import base

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from base.models import BaseModel

from intineratour import utilies as ut
#-- Import User Model




def user_filename(self, filename):
    url = "accounts_picture/%s/%s" % (self.id, filename)
    return url

#-- Create_user extendido de AbstractBaseUser
class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        user = self.model(
            email=self.normalize_email(email),
            is_active=False,
        )
        return user

#-- Clase abstracta extendida del modelo User
class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, db_index=True)
    sex = models.CharField(max_length=20, blank=True)
    nationality = models.CharField(max_length=30, blank=True)
    #-- Atributos adicionales
    phone = models.CharField(max_length=10)
    picture = models.ImageField(upload_to=user_filename, blank=True)
    user_type = models.CharField(max_length=2, choices=ut.USERTYPES_CHOICES, default='A')
    api_token = models.CharField(max_length=50, default='')
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
    	return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        db_table = 'users'

#-- Clase extendia del User para control de las llaves de activacion (Activacion / Solicitud de Contraseña / Invitacion)
class UserRequest(models.Model):
    user = models.ForeignKey(base.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=False)
    #-- Keys para la validacion por email cuando de crea el usuario
    activation_key = models.CharField(max_length=40, blank=True)
    expires_key = models.DateTimeField(default=datetime.now)
    activation_type = models.CharField(max_length=2, choices=ut.ACTIVATION_CHOICES, default='1')
    activation_status = models.CharField(max_length=2, choices=ut.ACTIVATIONSTATUS_CHOICES, default='0')
    activation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users_request'


# Create your models here.
