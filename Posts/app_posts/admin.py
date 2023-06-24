from django.contrib import admin
from .models import Post, Comment, Topic


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ["title__startswith"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title']
