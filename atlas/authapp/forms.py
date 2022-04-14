from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password1','password2')
        widgets = {
            'username': forms.EmailInput(attrs={'class': 'form-control form-control-user',
                                               'id':'exampleInputEmail',
                                               'placeholder':'username'
                                               }),
        }
        password1 = forms.CharField(widget=forms.PasswordInput(
            attrs={'class': 'form-control form-control-user', 'type': 'password', 'name': 'password','id':'exampleInputPassword', 'placeholder': 'Password'}),
            label='')
        password2 = forms.CharField(widget=forms.PasswordInput(
            attrs={'class': 'form-control form-control-user', 'type': 'password', 'name': 'password','id':'exampleRepeatPassword', 'placeholder': 'Repeat Password'}),
            label='')