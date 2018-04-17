from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^(?P<category_id>[0-9]+)/$', views.product_category, name="product_category"),
	url(r'^list/$', views.products, name="products"),
]