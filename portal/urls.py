from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.DashboardView.as_view(), name='index'),
    path('login', views.loginuser, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('register', views.registeruser, name='register'),
    path('support', views.support, name='support'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('profile/<str:username>', views.ProfileView.as_view(), name='profileview'),
    path('article/<int:id>', views.ArticleView.as_view(), name='article'),
    path('favourite', views.toggleFavourite, name='favourite'),
    path('comment', views.Comment.as_view(), name='comment'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('delete', views.deleteArticle, name='delete')


]