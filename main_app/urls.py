from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('jewelry/', views.jewelry),
    path('beauty/', views.beauty),
    path('posts/', views.PostIndex.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('posts/new/', views.PostCreate.as_view()),
    path('posts/<int:post_id>/add_photo/', views.add_photo, name='add_photo'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view()),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view()),
    path('accounts/register/', views.register),
    path('search_posts', views.search_posts, name='search-posts'),
    path('posts/<int:pk>/comment', views.AddCommentView.as_view(), name='add-comment'),
    path('like/<int:pk>/', views.LikeView, name='like-post')
]

