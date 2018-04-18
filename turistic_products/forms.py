# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms import Form, ModelForm

from categories.models import Category
from turistic_products.models import TuristicProduct

class ProductForm(ModelForm):
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
		label = 'Description',
		min_length = 2,
		widget = forms.TextInput(
			attrs = {
				'class':'form-control'
			}
		)
	)


	price = forms.FloatField(
		label = 'precio',
		widget = forms.NumberInput(
			attrs = {
				'class':'form-control'
			}
		)
	)

	category = forms.ModelChoiceField(
		empty_label = 'Seleccione una categoria',
		queryset = Category.objects.filter(status=1),
		widget = forms.Select(
			attrs = {
				'class':'form-control'
			}
		)
	)

	class Meta:
		model = TuristicProduct
		fields = ('name', 'description', 'price', 'category', 'calification',)

