from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send/email/', views.send_email, name='send_email'),
    path('login/', views.login, name='login'),
    path('register/', views.signup, name='signup'),
    path('logout/', views.logOut, name='logout'),
    path('posts/', views.posts, name='posts'),
    path('post/<str:post_name>/', views.postDetail, name='post_detail'),
    path('create/post/', views.createPost, name='create_post'),
    path('update/post/<str:post_name>/', views.editPost, name='post_edit'),
    path('profile/<str:user_name>/', views.profile, name='profile'),
]