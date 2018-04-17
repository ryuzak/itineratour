# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from base.models import BaseModel
from categories.models import Category

# Create your models here.
class TuristicProduct(BaseModel):
	name = models.CharField(max_length=150)
	description = models.CharField(max_length=512)
	calification = models.FloatField(default=0)
	latitude = models.FloatField(default=0)
	longitude = models.FloatField(default=0)
	price = models.FloatField(default=0)
	category = models.ForeignKey(Category)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name