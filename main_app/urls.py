from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('jewelry/', views.jewelry),
    path('beauty/', views.beauty),
    path('posts/', views.PostIndex.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/new/', views.PostCreate.as_view()),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view()),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view()),
    path('accounts/register/', views.register),
    path('search_posts', views.search_posts, name='search-posts'),
]

urlpatterns += staticfiles_urlpatterns()