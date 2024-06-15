from django.contrib import admin

from .models import Chat


class ChatAdmin(admin.ModelAdmin):
    model = Chat
    list_display = [
        "pk",
        "sender",
        "receiver",
        "status",
        "message",
        "edited",
        "created_at",
        "updated_at",
    ]
    ordering = ["created_at"]


admin.site.register(Chat, ChatAdmin)
