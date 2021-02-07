from django.contrib import admin


class BaseNodeAdmin(admin.ModelAdmin):
    fields = ("id", "url", "name", "server_token", "client_token")
    readonly_fields = ("id", "server_token")


class BaseOrderAdmin(admin.ModelAdmin):
    def post_save_hook(
        self, obj_pk, celery_publisher, serialized_obj, dest_url, obj_lookup_value
    ):
        if obj_pk:  # update was performed
            method = "PUT"
        else:  # create was performed
            method = "POST"
        celery_publisher.send_task(
            "core.tasks.sync_order",
            retry=True,
            retry_policy={
                "max_retries": 3,
                "interval_start": 3,
                "interval_step": 1,
                "interval_max": 6,
            },
            args=[dest_url, serialized_obj, obj_lookup_value, method],
        )

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
