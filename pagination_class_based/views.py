from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['id']
    paginate_by = 3
    paginate_orphans = 1
