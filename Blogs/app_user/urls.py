from django.urls import path
from .views import Login, Registration, Logout, PasswordChange, Profile

urlpatterns = [
    path('login/', Login.as_view(), name="my_login"),
    path('logout/', Logout.as_view(), name="my_logout"),
    path('registration/', Registration.as_view(), name="get_registration"),
    path('change/', PasswordChange.as_view(), name="password_change"),
    path('profile/<str:username>/', Profile.as_view(), name="profile"),
]
