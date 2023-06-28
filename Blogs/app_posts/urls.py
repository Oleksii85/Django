from django.urls import path
from .views import PostCreate, CommentCreate, PostsListView, PostDetailView, TopicsListView, TopDetailView, \
    PostUpdate, PostDelete, info_site, LikePost, Subscribe

urlpatterns = [
    path('', TopicsListView.as_view(), name="get_all_topic"),
    path('<slug:slug>/subscribe', Subscribe.as_view(), name="subscriptions"),
    path('posts/', PostsListView.as_view(), name="get_all_posts"),
    path('create/', PostCreate.as_view(), name="post_create"),
    path('about/', info_site, name="info_site"),
    path('<slug:slug>/update/', PostUpdate.as_view(), name="post_update"),
    path('<slug:slug>/delete/', PostDelete.as_view(), name="post_delete"),
    path('<slug:slug>/comment/', CommentCreate.as_view(), name="create_comment"),
    path('topic/<slug:slug>/', TopDetailView.as_view(), name="get_topic"),
    path('<slug:slug>/', PostDetailView.as_view(), name="get_post"),
    path('post/<slug:slug>/like', LikePost.as_view(), name='like_post')
]
