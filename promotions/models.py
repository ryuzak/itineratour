# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from base.models import BaseModel
from turistic_products.models import TuristicProduct
# Create your models here.

class Promotion(BaseModel):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=512)
	product = models.ForeignKey(TuristicProduct)
	porcentage = models.FloatField(default=0)
	final_price = models.FloatField(default=0)

	class Meta:
		db_table = 'promotions'
