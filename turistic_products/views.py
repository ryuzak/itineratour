# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse

from turistic_products.forms import ProductForm
from turistic_products.models import TuristicProduct
import json

# Create your views here.

def product_add(request):
	form = ProductForm()
	if request.POST:
		form = ProductForm(request.POST)
		print form
		if form.is_valid():
			model = form.save()
			return redirect('turistic_products:products')
	return render(request, 'turistic_products/product.html', {'form':form})

def product_add_async(request):
	form = ProductForm()
	if request.POST:
		form = ProductForm(request.POST)
		if form.is_valid():
			model = form.save()
			return HttpResponse(json.dumps({'status':'OK'}))
	return HttpResponse(json.dumps({'status':'ERROR'}))

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
