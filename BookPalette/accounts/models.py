from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_color = models.CharField(max_length=7, default="#cccccc")
    favorite_categories = models.ManyToManyField("books.Category", blank=True, related_name="users_favorited")
