from django.contrib import admin

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser

    list_display = [
        "full_name",
        "phone_number",
        "is_driver",
        "driver_license",
        "rating",
        "password",
    ]

    search_fields = [
        "full_name",
        "phone_number",
    ]

    ordering = ["full_name"]


admin.site.register(CustomUser, CustomUserAdmin)
