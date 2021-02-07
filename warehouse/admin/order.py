from core.admin import BaseOrderAdmin
from warehouse.celery import celery_app
from warehouse.serializers import OrderSerializer


class OrderAdmin(BaseOrderAdmin):
    fields = ("id", "number", "status", "store")

    def get_readonly_fields(self, request, obj=None):
        base_readonly_fields = ("id",)
        if obj:
            return base_readonly_fields + (
                "number",
                "store",
            )
        return base_readonly_fields

    def save_model(self, request, obj, form, change):
        obj_pk = obj.pk
        order_serialized = OrderSerializer(instance=obj).data
        super().save_model(request, obj, form, change)
        self.post_save_hook(
            obj_pk, celery_app, order_serialized, obj.store.url, obj.number
        )
