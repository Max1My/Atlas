from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib import auth

from .forms import RegisterUserForm,LoginUserForm
from .utils import DataMixin


class RegisterUser(DataMixin,CreateView):
    form_class = RegisterUserForm
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('authapp:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'authapp/login.html'

    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))