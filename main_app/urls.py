from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    # path('posts/', views.posts_index),
    path('posts/', views.PostIndex.as_view()),
   
]