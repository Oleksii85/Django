from django.shortcuts import render, get_object_or_404
from .models import Blogpost, Comment


def get_post(request, slug):
    post = get_object_or_404(Blogpost, slug=slug)
    comments = Comment.objects.filter(blogpost__title=post.title)
    return render(request, "post_detail.html", {"post": post, "comment": comments})


def get_all_posts(request):
    posts = Blogpost.objects.all()
    return render(request, "posts.html", {"posts": posts})
