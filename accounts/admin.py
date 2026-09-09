from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class user_admin(UserAdmin):
    list_display = (
        "username",
        "email",
        "password"
    )

