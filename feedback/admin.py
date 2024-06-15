from django.contrib import admin

from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = [
        "ride",
        "passenger",
        "driver",
        "rating",
        "feedback",
    ]

    ordering = ["rating"]


admin.site.register(Feedback, FeedbackAdmin)
