from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class FollowersCount(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length=100)
    title = models.TextField()
    desc = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class LikesCount(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username