from django.urls import path
from . import views

#Add our index to root path
urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
]