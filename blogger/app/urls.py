from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.PostListView.as_view(), name='posts'),
    path('blogs/<int:pk>/', views.PostDetailView.as_view(), name='posts.details'),
    path('blogs/popular/', views.PopularPostListView.as_view(), name='popular_posts'),
    path('blogs/create/', views.PostCreateView.as_view(), name='posts.new'),
]