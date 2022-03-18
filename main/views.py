from django.shortcuts import render

# Create your views here.
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'main/index.html', {'posts': posts})

