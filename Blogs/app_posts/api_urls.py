from .api_view import PostViewSet, TopicViewSet, CommentViewSet
from rest_framework import routers

urlpatterns = [
]

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'topics', TopicViewSet)
router.register(r'comments', CommentViewSet)
urlpatterns += router.urls
