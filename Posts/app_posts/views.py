from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Post, Comment, Topic
from .forms import CommentModelForm, PostModelForm


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment"] = Comment.objects.filter(post=self.object)
        context["form"] = CommentModelForm()
        return context


class PostsListView(ListView):
    model = Post
    template_name = "posts.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset().order_by('title')
        if "search" in self.request.GET:
            queryset = queryset.filter(title__iregex=self.request.GET["search"])
        return queryset


class TopDetailView(DetailView):
    model = Topic
    template_name = "top_list.html"
    context_object_name = "topic"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.filter(topic=self.object).order_by('title')
        if "search" in self.request.GET:
            posts = posts.filter(title__iregex=self.request.GET["search"])
        context["posts"] = posts
        return context


class TopicsListView(ListView):
    model = Topic
    template_name = "topic.html"
    context_object_name = "topic"


class PostCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = PostModelForm
    template_name = "create_post.html"
    success_url = reverse_lazy('get_all_posts')
    success_message = "Пост %(title)s створено"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class CommentCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CommentModelForm
    template_name = "create_comment.html"
    success_url = reverse_lazy('get_all_posts')
    success_message = "Додано новий коментар"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'topic']
    template_name = "post_update.html"
    success_url = reverse_lazy('get_all_posts')
    success_message = "Пост %(title)s змінено"


class PostDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy('get_all_posts')
    success_message = "Пост видалено"
