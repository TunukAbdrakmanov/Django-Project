from django.urls import path

from .views import index

urlpatterns = [
    path('posts/', index),
]