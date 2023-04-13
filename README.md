# Social-Media-App---Backend
Social Media App Developed in Django


urlpatterns = [
    path('api/authenticate', views.UserAPIView.as_view(), name='authenticate'),
    path('api/follow/<str:pk>', views.follow, name='follow'),
    path('api/unfollow/<str:pk>', views.unfollow, name='unfollow'),
    path('api/user/', views.profile, name='profile'),
    path('api/posts/', views.upload, name='upload'),
    path('api/posts/<uuid:pk>', views.delete, name='delete'),
    path('api/like/<uuid:pk>', views.like, name='like'),
    path('api/unlike/<uuid:pk>', views.unlike, name='unlike'),
    path('api/comment/<uuid:pk>', views.comment, name='comment'),
    path('api/posts/<uuid:pk>', views.post_details, name='post'),
    path('api/all_posts', views.all_posts, name='all_posts'),
]

all Paths
