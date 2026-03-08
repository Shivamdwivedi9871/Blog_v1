from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_commets')
    text = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post) + '|' + str(self.author)
