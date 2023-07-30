# Social-Media-App-Backend-APIs

Social Media App Developed in Django

Here are the URL patterns for our API:

## To authenticate users, use the path 'api/authenticate' and the view 'UserAPIView' with the name 'authenticate'.
**Endpoint:** '/api/authenticate'
    path('api/authenticate', views.UserAPIView.as_view(), name='authenticate')

## To follow a user, use the path 'api/follow/<str:pk>' with the view 'follow' and the name 'follow'.
**Endpoint:** '/api/follow/<str:pk>'
    path('api/follow/<str:pk>', views.follow, name='follow')

## To unfollow a user, use the path 'api/unfollow/<str:pk>' with the view 'unfollow' and the name 'unfollow'.
**Endpoint:** '/api/unfollow/<str:pk>'
    path('api/unfollow/<str:pk>', views.unfollow, name='unfollow')

##To view a user's profile, use the path 'api/user/' with the view 'profile' and the name 'profile'.
**Endpoint:** '/api/user/'
    path('api/user/', views.profile, name='profile')

##To upload a post, use the path 'api/posts/' with the view 'upload' and the name 'upload'.
**Endpoint:** '/api/posts/'
    path('api/posts/', views.upload, name='upload')

##To delete a post, use the path 'api/posts/<uuid:pk>' with the view 'delete' and the name 'delete'.
**Endpoint:** '/api/posts/<uuid:pk>'
    path('api/posts/<uuid:pk>', views.delete, name='delete')

##To like a post, use the path 'api/like/<uuid:pk>' with the view 'like' and the name 'like'.
**Endpoint:** '/api/like/<uuid:pk>'
    path('api/like/<uuid:pk>', views.like, name='like')

##To unlike a post, use the path 'api/unlike/<uuid:pk>' with the view 'unlike' and the name 'unlike'.
**Endpoint:** '/api/unlike/<uuid:pk>'
    path('api/unlike/<uuid:pk>', views.unlike, name='unlike')

##To comment on a post, use the path 'api/comment/<uuid:pk>' with the view 'comment' and the name 'comment'.
**Endpoint:** '/api/comment/<uuid:pk>'
    path('api/comment/<uuid:pk>', views.comment, name='comment')

##To view the details of a post, use the path 'api/posts/<uuid:pk>' with the view 'post_details' and the name 'post'.
**Endpoint:** '/api/posts/<uuid:pk>'
    path('api/posts/<uuid:pk>', views.post_details, name='post')

##To view all posts, use the path 'api/all_posts' with the view 'all_posts' and the name 'all_posts'.
**Endpoint:** '/api/all_posts'
    path('api/all_posts', views.all_posts, name='all_posts') 

These are the URL patterns for our API, including paths and views for authentication, following and unfollowing users, uploading and deleting posts, liking and commenting on posts, and viewing post details and all posts.
