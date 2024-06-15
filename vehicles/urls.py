from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.vehicle_register),
    path("update/", views.update_vehicle_detail),
]
