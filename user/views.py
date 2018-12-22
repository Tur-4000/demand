from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, PasswordChangeView


class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('demand_list')


class UserLoginView(LoginView):
    template_name = 'user/login.html'


class UserPasswordChangeView(PasswordChangeView):
    template_name = 'user/password_change.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('demand_list')
