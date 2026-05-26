from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from .forms import PostForm


# Create your views here.
# def home(request):
#     return HttpResponse("Health Check OK")

def add_like_view(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        post.likes += 1
        post.save()
    return HttpResponseRedirect(reverse('posts.details', kwargs={'pk': post.pk}))

def change_visibility_view(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        post.is_public = not post.is_public
        post.save()
    return HttpResponseRedirect(reverse('posts.details', kwargs={'pk': post.pk}))

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    context_object_name = 'Post'
    success_url = '/posts/blogs/'
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/update_post.html'
    form_class = PostForm
    success_url = '/posts/blogs/'

class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/create_post.html'
    form_class = PostForm
    success_url = '/posts/blogs/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/post_lists.html'
    context_object_name = 'Posts'

    def get_queryset(self):
        return self.request.user.posts.all().order_by('-created_at')

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_details.html'
    context_object_name = 'Post'
    login_url = '/admin/'

class PopularPostListView(ListView):
    model = Post
    template_name = 'posts/popular_posts.html'
    context_object_name = 'Posts'

    def get_queryset(self):
        return Post.objects.filter(likes__gt=1).order_by('-likes')

class Postviewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
