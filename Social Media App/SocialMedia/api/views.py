from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, LikesCount, FollowersCount, Comment
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import serializers
import jwt, datetime



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "password")

class UserAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


@login_required(login_url='api/authenticate')
def follow(request, pk):
    if request.method == 'POST':
        follower = request.user.username
        user = pk

        new_follower = FollowersCount.objects.create(follower=follower, user=user)
        new_follower.save()
        return None

    else:
        return None


@login_required(login_url='api/authenticate')
def unfollow(request, pk):
    if request.method == 'POST':
        follower = request.user.username
        user = pk

        delete_follower = FollowersCount.objects.get(follower=follower, user=user)
        delete_follower.delete()
        return None
    else:
        return None


@login_required(login_url='api/authenticate')
def profile(request):
    pk = request.user.username
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_bio = user_profile.bio

    follower = request.user.username
    user = pk

    user_followers = len(FollowersCount.objects.filter(user=pk))
    user_following = len(FollowersCount.objects.filter(follower=pk))

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_bio': user_bio,
        'user_followers': user_followers,
        'user_following': user_following,
    }
    return render(request, '', context)


@login_required(login_url='api/authenticate')
def upload(request):
    if request.method == 'POST':
        user = request.user.username
        title = request.POST['title']
        desc = request.POST['desc']

        new_post = Post.objects.create(user=user, image=title, caption=desc)


        context = {
            'post_id': new_post.id,
            'title': new_post.title,
            'description': new_post.desc,
            'created_time': new_post.created_at,
        }

        return render(request, "", context=context)
    else:
        return None


@login_required(login_url='api/authenticate')
def delete(request, pk):
    if request.method == 'DELETE':
        post = Post.objects.get(id=pk)
        if post.user == request.user:
            post.delete()

        return None
    else:
        return None


@login_required(login_url='api/authenticate')
def like(request, pk):
    username = request.user.username
    post_id = pk

    post = Post.objects.get(id=post_id)

    new_like = LikesCount.objects.create(post_id=post_id, username=username)
    new_like.save()
    post.no_of_likes = post.no_of_likes+1
    post.save()
    return None


@login_required(login_url='api/authenticate')
def unlike(request, pk):
    username = request.user.username
    post_id = pk

    post = Post.objects.get(id=post_id)

    like_filter = LikesCount.objects.filter(post_id=post_id, username=username).first()
    like_filter.delete()
    post.no_of_likes = post.no_of_likes-1
    post.save()
    return None


@login_required(login_url='api/authenticate')
def comment(request, pk):
    if request.method == 'POST':
        post_id = pk
        comment = request.POST["comment"]
        user = request.user.username

        new_comment = Comment.objects.create(post_id=post_id , comment=comment, username=user,)
        new_comment.save()
        comment_id=comment.id
        context={
            "comment_id": comment_id,
        }

        return render(request,"", context)
    else:
        return None


@login_required(login_url='api/authenticate')
def post_details(request, pk):
    post_id = pk

    post = Post.objects.get(id=post_id)

    likes = post.no_of_likes
    comments = Comment.objects.filter(id=post_id)
    no_of_comments = len(comments)

    context = {"post": post,
               "likes": likes,
               "no_of_comments": no_of_comments,
               "comments": comments
    }
    return render(request, "", context)


@login_required(login_url='api/authenticate')
def all_posts(request):
    user = request.user.username

    all_post = Post.objects.filter(user).order_by("-created_at")

    posts = []

    for post_obj in all_post:
        obj = {
            'post_id': post_obj.id,
            'title': post_obj.title,
            'desc': post_obj.desc,
            'created_at': post_obj.created_at,
            'likes': post_obj.no_of_likes,
            "comments": Comment.objects.filter(post_id=post_obj.id),
        }
        posts.append(obj)

    context = {"posts": posts}

    return render(request, "", context)

