from django.urls import path
from .views import index, login, registration, details, create

urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name="login"),
    path('registration/', registration, name="registration"),
    path('details/', details, name="details"),
    path('create/', create, name="create"),
]
