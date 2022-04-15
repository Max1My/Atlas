from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy

from .forms import RegisterUserForm
from .utils import DataMixin


class RegisterUser(DataMixin,CreateView):
    form_class = RegisterUserForm
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('authapp:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))