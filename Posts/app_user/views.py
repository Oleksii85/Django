from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView


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
