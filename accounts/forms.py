from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import User

class Register_form(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', "password1", "password2")

class User_change_admin_form(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email", 'password')

class Login_form(AuthenticationForm):
    pass