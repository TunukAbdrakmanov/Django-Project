from django.db import models

# Create your models here.
from main.models import Post


class Comment(models.Model):
    author = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {self.text}
