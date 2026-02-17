from django.urls import path
from .views import register_view, dashboard,post_login_redirect
from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_view, post_login_redirect, logout_view

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html"
        ),
        name="login",
    ),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("redirect/", post_login_redirect, name="post_login_redirect"),
]
