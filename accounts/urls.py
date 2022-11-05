from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup", views.signup, name="signup"),
]
