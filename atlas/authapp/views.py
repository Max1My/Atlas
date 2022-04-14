from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse, reverse_lazy

from .forms import RegisterUserForm


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('login')
