from django.urls import path

from . import views

urlpatterns = [
    path("inbox/", views.get_inbox),
    path("send/", views.send_message),
    path("delete/<str:pk>/", views.delete_message),
    path("update/<str:pk>/", views.update_message),
    path("detail/<str:pk>/", views.get_chat_detail),
]
