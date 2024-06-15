from django.contrib import admin

from .models import Ride, RideHistory


class RideAdmin(admin.ModelAdmin):
    model = Ride

    list_display = [
        "vehicle",
        "status",
        "number_of_passengers",
        "current_location",
        "created_at",
        "updated_at",
    ]
    ordering = ["created_at"]


class RideHistoryAdmin(admin.ModelAdmin):
    class Meta:
        model = RideHistory

    list_display = [
        "passenger",
        "ride",
        "pickup_location",
        "drop_location",
        "created_at",
        "updated_at",
    ]


admin.site.register(Ride, RideAdmin)
admin.site.register(RideHistory, RideHistoryAdmin)
