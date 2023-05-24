from django.urls import path
from .views import blogs, about, slugs, comment, create, update, delete, profile, change_pass, register, login, logout

urlpatterns = [
    path("blogs/", blogs),
    path("", blogs),
    path("about/", about),
    path("<slug:slug>/comment/", comment),
    path("create/", create),
    path("<slug:slug>/update/", update),
    path("<slug:slug>/delete/", delete),
    path("profile/<str:username>/", profile),
    path("change_password/", change_pass),
    path("register/", register),
    path("login/", login),
    path("logout/", logout),
    path("<slug:slug>/", slugs),
]