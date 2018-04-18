# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms import Form, ModelForm

from .models import Promotion
from turistic_products.models import TuristicProduct

class PromotionForm(ModelForm):
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
		label = 'Descripcion',
		min_length = '2',
		widget = forms.TextInput(
			attrs = {
				'class':'form-control'
			}
		)
	)

	porcentage = forms.FloatField(
		label = 'Procentaje',
		widget = forms.NumberInput(
			attrs = {
				'class':'form-control'
			}
		)
	)

	final_price = forms.FloatField(
		label = 'Precio final',
		widget = forms.NumberInput(
			attrs = {
				'class':'form-control'
			}
		)
	)

	product = forms.ModelChoiceField(
		empty_label = 'selecione un producto',
		queryset = TuristicProduct.objects.filter(status=1),
		widget = forms.Select(
			attrs = {
				'class':'form-control'
			}
		)
	)

	class Meta:
		model = Promotion
		fields = ('name', 'description', 'porcentage', 'final_price', 'product')