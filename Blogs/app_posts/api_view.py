from rest_framework import viewsets
from .models import Post, Topic, Comment
from .serializers import PostModelSerializer, TopicModelSerializer, CommentModelSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicModelSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer
