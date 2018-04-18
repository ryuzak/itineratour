from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^list/$', views.category_list, name="category_list"),
	url(r'^add/$', views.category_add, name='category_add'),
]