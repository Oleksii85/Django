from django.urls import path
from .views import my_login, logout_view, get_registration

urlpatterns = [
    path('', my_login, name="my_login"),
    path('logout/', logout_view, name="my_logout"),
    path('registration/', get_registration, name="get_registration"),
]
