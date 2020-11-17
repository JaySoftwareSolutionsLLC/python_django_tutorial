from django.shortcuts import render
from django.views.generic import ListView
from . models import Post

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts' # Default is object_list?
    ordering = ['-date_posted']

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) # Directly passing context

