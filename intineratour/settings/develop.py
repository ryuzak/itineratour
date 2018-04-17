 # -- develop.py
from .base import *


DEBUG = True
ALLOWED_HOSTS = ['192.168.1.190','localhost', '192.168.11.102']

INSTALLED_APPS += (
	'accounts',
	'authorization',
	'recovery',
	'base',
	'categories',
	'turistic_products',
	'promotions',
)