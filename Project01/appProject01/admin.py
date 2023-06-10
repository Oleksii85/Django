from django.contrib import admin
from .models import Author, Blogpost, Comment, Topic


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ['title'] + ['get_time']
    search_fields = ["title__startswith"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content'] + ['get_time']


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title']
