from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#Add our index to root path
urlpatterns = [
    path('', views.index, name = 'index'),
]