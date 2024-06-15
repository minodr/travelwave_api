from django.urls import path

from . import views

urlpatterns = [
    path("", views.available_rides),
    path("cancel/", views.cancel_ride),
    path("create/", views.create_ride),
    path("<str:id>/", views.get_ride_detail),
    path("location/", views.get_ride_detail),
    path("<str:id>/passengers/", views.get_ride_passengers),
    path("<str:id>/passengers/remove", views.remove_passenger),
    path("<str:id>/passengers/add/", views.add_passenger),
    path("<str:id>/update/", views.update_ride_detail),
    path("pick/", views.pick_ride),
]

"""
    api/rides/
        - create ride
        - get list of rides

    api/rides/id/ 
        - get ride detail
        - update ride detail
        - cancel ride

    api/rides/id/passengers/
        - list passengers of a ride
        - add passenger to the ride
        - remove a passenger from a ride

    api/rides/pick/
        - pick one ride from available rides
"""
