from django.contrib import admin
from .models import Profile, Post, LikesCount, FollowersCount, Comment


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikesCount)
admin.site.register(FollowersCount)
admin.site.register(Comment)