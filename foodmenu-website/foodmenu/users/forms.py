from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    # Meta is a class that provide information about the main class

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']




