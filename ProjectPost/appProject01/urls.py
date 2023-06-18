from django.urls import path
from .views import PostCreate, CommentCreate, PostsListView, PostDetailView, TopicsListView, TopListView

urlpatterns = [
    path('', TopicsListView.as_view(), name="get_all_topic"),
    path('posts/', PostsListView.as_view(), name="get_all_posts"),
    path('form/', PostCreate.as_view(), name="post_form"),
    path('comment/', CommentCreate.as_view(), name="create_comment"),
    path('topic/<slug:slug>', TopListView.as_view(), name="get_topic"),
    path('<slug:slug>', PostDetailView.as_view(), name="get_post"),
]
