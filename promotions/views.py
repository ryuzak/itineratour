# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Promotion
from .forms import PromotionForm
# Create your views here.

def promotion_list_async(request):
	promotions = Promotion.objects.filter(status=1)
	promotion_list = []
	for promotion in promotions:
		promotion_list.append({
			'name':promotion.name,
			'description':promotion.description,
			'product':promotion.product.name,
			'porcentage':promotion.porcentage,
			'final_price':promotion.final_price
		})
	return HttpResponse(json.dumps(promotion_list))

def promotion_list(request):
	promotions = Promotion.objects.filter(status=1)
	return render(request, 'promotions/promotion_list.html', {'promos':promotions})

def promotion_add(request):
	form = PromotionForm()
	if request.POST:
		form = PromotionForm(request.POST)
		if form.is_valid():
			model = form.save()
			return redirect('promotions:promotion_list')
	return render(request, 'promotions/promotion.html',{'form':form})
