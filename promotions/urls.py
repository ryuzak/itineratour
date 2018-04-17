from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^list/$', views.promotion_list, name="promotion_list"),
	url(r'^list_async/$', views.promotion_list_async, name="promotion_list_async"),
	url(r'^add/$', views.promotion_add, name='promotion_add'),
]