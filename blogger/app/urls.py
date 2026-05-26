from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.PostListView.as_view(), name='posts'),
    path('blogs/<int:pk>/', views.PostDetailView.as_view(), name='posts.details'),
    path('blogs/<int:pk>/edit/', views.PostUpdateView.as_view(), name='posts.update'),
    path('blogs/<int:pk>/delete/', views.PostDeleteView.as_view(), name='posts.delete'),
    path('blogs/popular/', views.PopularPostListView.as_view(), name='popular_posts'),
    path('blogs/create/', views.PostCreateView.as_view(), name='posts.new'),
    path('blogs/<int:pk>/like/', views.add_like_view, name='posts.add_like'),
    path('blogs/<int:pk>/toggle_visibility/', views.change_visibility_view, name='posts.toggle_visibility'),
]