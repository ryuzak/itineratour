from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^(?P<category_id>[0-9]+)/$', views.product_category, name="product_category"),
	url(r'^list/$', views.products, name="products"),
	url(r'^add/$', views.product_add, name="product_add"),
	url(r'^add/async/$', views.product_add_async, name="product_add_async"),
]