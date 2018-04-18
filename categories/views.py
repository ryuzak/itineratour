# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .forms import CategoryForm
from .models import Category

# Create your views here.
def category_add(request):
	form = CategoryForm()
	if request.POST:
		form = CategoryForm(request.POST)
		if form.is_valid():
			model = form.save()
			return redirect('categories:category_list')
	return render(request, 'categories/category.html', {'form':form})

def category_list(request):
	cate_list = Category.objects.all()
	return render(request, 'categories/category_list.html', {'categories':cate_list})