from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from app_posts.models import Post, Comment, Topic


class Login(SuccessMessageMixin, LoginView):
    success_url = reverse_lazy('get_all_topic')
    template_name = 'login.html'
    success_message = "Ви увійшли в кабінет як: %(username)s "

    def get_success_url(self):
        return self.success_url


class Registration(SuccessMessageMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('my_login')
    success_message = "Створено %(username)s користувача"


class Logout(LoginRequiredMixin, LogoutView):
    next_page = 'my_login'
    login_url = ''


class PasswordChange(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'password_change.html'
    success_url = reverse_lazy('get_all_topic')
    success_message = "Користувач %(username)s змінив пароль"


class Profile(LoginRequiredMixin, ListView):
    model = User
    template_name = "profile.html"
    context_object_name = "author"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(author=self.request.user).order_by('title')
        context["comments"] = Comment.objects.filter(author=self.request.user).order_by('created_at')
        context["likes"] = Post.objects.filter(likes=True).order_by('title')
        context["subscribe"] = Topic.objects.filter(subscribe=True).order_by('title')
        return context
