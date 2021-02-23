from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(views.DashboardView.as_view()), name='index'),
    path('login', views.loginuser, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('register', views.registeruser, name='register'),
    path('support', views.support, name='support'),
    path('profile', login_required(views.ProfileView.as_view()), name='profile'),
    path('profile/<str:username>', login_required(views.ProfileView.as_view()), name='profileview'),
    path('article/<int:id>', views.articleView, name='article'),
    path('favourite', views.toggleFavourite, name='favourite'),
    path('comment', views.Comment.as_view(), name='comment')


]