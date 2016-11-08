from django.contrib.auth.models import User
from django.db import models


class Tweet(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
