from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.login_user),
    path("register/", views.register_user),
    path("logout/", views.logout_user),
    path("profile/", views.get_user_data),
    path("delete/", views.delete_user_account),
    path("change-password/", views.change_user_password),
    path("update-profile/", views.update_user_profile),
]
