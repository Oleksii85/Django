from django.urls import path
from .views import Login, Registration, Logout, PasswordChange

urlpatterns = [
    path('login/', Login.as_view(), name="my_login"),
    path('logout/', Logout.as_view(), name="my_logout"),
    path('registration/', Registration.as_view(), name="get_registration"),
    path('change/', PasswordChange.as_view(), name="password_change"),
]
