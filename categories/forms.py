# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms import Form, ModelForm

from .models import Category

class CategoryForm(ModelForm):
	name = forms.CharField(
		label = 'Nombre',
		min_length = 2,
		widget = forms.TextInput(
			attrs = {
				'class':'form-control'
			}
		)
	)

	description = forms.CharField(
		label = 'Descriptcion',
		min_length = 2,
		widget = forms.TextInput(
			attrs = {
				'class':'form-control'
			}
		)
	)

	class Meta:
		model = Category
		fields = ('name','description',)