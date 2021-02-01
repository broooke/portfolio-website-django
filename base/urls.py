from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send/email/', views.send_email, name='send_email'),
    path('login/', views.login, name='login'),
    path('register/', views.signup, name='signup'),
    path('logout/', views.logOut, name='logout'),
    path('posts/', views.posts, name='posts'),
]