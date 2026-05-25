from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView


# Create your views here.
# def home(request):
#     return HttpResponse("Health Check OK")

class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/create_post.html'
    fields = ['title', 'content']
    success_url = '/posts/blogs/'


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_lists.html'
    context_object_name = 'Posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_details.html'
    context_object_name = 'Post'

class PopularPostListView(ListView):
    model = Post
    template_name = 'posts/popular_posts.html'
    context_object_name = 'Posts'

    def get_queryset(self):
        return Post.objects.filter(likes__gt=1).order_by('-likes')


class Postviewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
