
from django.urls import path
from .import views

urlpatterns = [
    path('', views.tweet_list,name='tweet_list'),
    path('create/', views.create_tweet,name='create_tweet'),
    path('edit_tweet/<int:pk>/', views.edit_tweet,name='edit_tweet'),
    path('delete_tweet/<int:pk>/', views.delete_tweet,name='delete_tweet'),
    path('register/', views.register,name='register'),
    path("search/", views.search_bar, name="search_bar"),
    path('like_tweet/<int:pk>/', views.like_tweet,name='like_tweet'),
    path('add_comment/<int:pk>/', views.add_comment,name='add_comment'),
    path('profile/<str:username>/',views.profile_view,name='profile_view')
    
]