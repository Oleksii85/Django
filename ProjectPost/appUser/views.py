from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView


class Login(LoginView):
    success_url = 'topic/'
    template_name = 'login.html'

    def get_success_url(self):
        return self.success_url


class Registration(CreateView):
    form_class = UserCreationForm
    template_name = 'registration.html'
    success_url = 'topic/'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = 'my_login'
    login_url = ''
