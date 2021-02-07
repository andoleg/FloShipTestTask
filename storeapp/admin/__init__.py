from django.contrib import admin

from core.admin import BaseNodeAdmin
from storeapp.admin.order import OrderAdmin
from storeapp.models import Order, Warehouse

admin.site.register(Order, OrderAdmin)
admin.site.register(Warehouse, BaseNodeAdmin)
