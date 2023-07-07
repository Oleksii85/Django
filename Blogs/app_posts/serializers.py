from django.utils.text import slugify
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Post, Topic, Comment


class PostModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ["title", "content", "author", "topic"]

    def validate(self, attrs):
        val_title = attrs["title"]
        slug = slugify(val_title)
        slugs = Post.objects.filter(slug__istartswith=slug).exists()
        if slugs:
            raise ValidationError("Такий слаг вже є!")
        return attrs


class TopicModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topic
        fields = ["title", "description"]


class CommentModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ["content", "author", "post"]
