from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from .models import Blogpost, Comment, Topic
from .forms import CommentModelForm, BlogpostModelForm


class PostDetailView(DetailView):
    model = Blogpost
    template_name = 'post_detail.html'
    context_object_name = "post", "comment"

    def get(self, request, slug):
        post = get_object_or_404(Blogpost, slug=slug)
        comments = Comment.objects.filter(blogpost__title=post.title)
        return render(request, "post_detail.html", {"post": post, "comment": comments})


class PostsListView(ListView):
    model = Blogpost
    template_name = "posts.html"
    context_object_name = "posts"

    def get(self, request):
        posts = Blogpost.objects.all()
        if "search" in request.GET:
            posts = Blogpost.objects.filter(title__iregex=request.GET["search"])
            return render(request, "posts.html", {"posts": posts})
        return render(request, "posts.html", {"posts": posts})


class TopListView(ListView):
    model = Blogpost
    template_name = "top_list.html"
    context_object_name = "posts", "topic"

    def get(self, request, slug):
        topic = get_object_or_404(Topic, slug=slug)
        posts = Blogpost.objects.filter(topic__title=topic.title).order_by('title')
        if "search" in request.GET:
            posts = Blogpost.objects.filter(title__iregex=request.GET["search"])
            return render(request, "top_list.html", {"topic": topic, "posts": posts})
        return render(request, "top_list.html", {"topic": topic, "posts": posts})


class TopicsListView(ListView):
    model = Topic
    template_name = "topic.html"
    context_object_name = "topic"


class PostCreate(CreateView):
    def get(self, request):
        form = BlogpostModelForm()
        return render(request, "create_post.html", context={"form": form})

    def post(self, request):
        form = BlogpostModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("get_all_posts")
        return render(request, "create_post.html", context={"form": form})


class CommentCreate(CreateView):
    def get(self, request):
        form = CommentModelForm()
        return render(request, "create_comment.html", context={"form": form})

    def post(self, request):
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comm = form.save(commit=False)
            comm.author = request.user
            comm.save()
            return redirect("get_all_posts")
        return render(request, "create_comment.html", context={"form": form})
