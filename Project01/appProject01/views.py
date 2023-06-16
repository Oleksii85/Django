from django.shortcuts import render, get_object_or_404, redirect
from .models import Blogpost, Comment, Topic
from .forms import CommentModelForm, BlogpostModelForm


def get_post(request, slug):
    post = get_object_or_404(Blogpost, slug=slug)
    comments = Comment.objects.filter(blogpost__title=post.title)
    return render(request, "post_detail.html", {"post": post, "comment": comments})


def get_all_posts(request):
    posts = Blogpost.objects.all()
    if "search" in request.GET:
        posts = Blogpost.objects.filter(title__iregex=request.GET["search"])
        return render(request, "posts.html", {"posts": posts})
    return render(request, "posts.html", {"posts": posts})


def get_topic(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    posts = Blogpost.objects.filter(topic__title=topic.title)
    if "search" in request.GET:
        posts = Blogpost.objects.filter(title__iregex=request.GET["search"])
        return render(request, "top_list.html", {"topic": topic, "posts": posts})
    return render(request, "top_list.html", {"topic": topic, "posts": posts})


def get_all_topic(request):
    topic = Topic.objects.all()
    return render(request, "topic.html", {"topic": topic})


def post_form(request):
    if request.method == "POST":
        form = BlogpostModelForm(request.POST)
        if form.is_valid():
            post = form.save()
            return get_all_posts(request)
        return render(request, "create_post.html", context={"form": form})
    form = BlogpostModelForm()
    return render(request, "create_post.html", context={"form": form})


def create_comment(request):
    if request.method == "POST":
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comm = form.save()
            return redirect("get_all_posts")
        return render(request, "create_comment.html", context={"form": form})
    form = CommentModelForm()
    return render(request, "create_comment.html", context={"form": form})



