from django.urls import path
from .views import Login, Registration, Logout
from appProject01.views import TopicsListView

urlpatterns = [
    path('', Login.as_view(), name="my_login"),
    path('logout/', Logout.as_view(), name="my_logout"),
    path('registration/', Registration.as_view(), name="get_registration"),
    path('registration/topic/', TopicsListView.as_view(), name="get_all_topic"),
]
