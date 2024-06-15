from django.contrib import admin

from .models import Vehicle


class VehicleAdmin(admin.ModelAdmin):
    model = Vehicle
    list_display = [
        "driver",
        "name",
        "make",
        "model",
        "year",
        "color",
        "license_plate",
        "number_of_seats",
    ]


admin.site.register(Vehicle, VehicleAdmin)
