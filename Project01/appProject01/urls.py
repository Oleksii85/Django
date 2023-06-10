from django.urls import path
from .views import get_all_posts, get_post

urlpatterns = [
    path('', get_all_posts, name="get_all_posts"),
    path('<slug:slug>', get_post, name="get_post")
]