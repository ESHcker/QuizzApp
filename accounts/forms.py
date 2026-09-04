from django import forms
from djano.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import User

# class register_form(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'email']

# class login_form(AuthenticationForm).
#     pass