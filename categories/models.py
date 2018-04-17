# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from base.models import BaseModel
# Create your models here.
class Category(BaseModel):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=512)