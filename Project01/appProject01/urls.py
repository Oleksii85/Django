from django.urls import path
from .views import get_all_posts, get_post, get_all_topic, get_topic, post_form, create_comment


urlpatterns = [
    path('topic/', get_all_topic, name="get_all_topic"),
    path('posts/', get_all_posts, name="get_all_posts"),
    path('form/', post_form, name="post_form"),
    path('comment/', create_comment, name="create_comment"),
    path('topic/<slug:slug>', get_topic, name="get_topic"),
    path('<slug:slug>', get_post, name="get_post"),
]
