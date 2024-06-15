from django.urls import path

from .views import rate

urlpatterns = [
    path("", rate),
]
