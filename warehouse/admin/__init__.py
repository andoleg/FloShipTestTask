from django.contrib import admin

from core.admin import BaseNodeAdmin
from warehouse.admin.order import OrderAdmin
from warehouse.models import Order, Store

admin.site.register(Order, OrderAdmin)
admin.site.register(Store, BaseNodeAdmin)
