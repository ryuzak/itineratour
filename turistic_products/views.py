# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from turistic_products.models import TuristicProduct
import json

# Create your views here.
def product_category(request, category_id):
	products = TuristicProduct.objects.filter(category_id=category_id)
	products_list = []
	print('hola')
	for product in products:
		products_list.append({
			'id':product.id,
			'name':product.name,
			'description':product.description,
			'calification':product.calification,
			'latitude':product.latitude,
			'longitude':product.longitude,
			'price':product.price,
			'category_id':product.category_id
		})
	json_list = {
		'products':products_list
	}
	return HttpResponse(json.dumps(json_list))


def products(request):
	products = TuristicProduct.objects.all()
	products_list = []
	print('hola')
	for product in products:
		products_list.append({
			'id':product.id,
			'name':product.name,
			'description':product.description,
			'calification':product.calification,
			'latitude':product.latitude,
			'longitude':product.longitude,
			'price':product.price,
			'category_id':product.category_id
		})
	json_list = {
		'products':products_list
	}
	return HttpResponse(json.dumps(json_list))
