from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView
                                , DetailView
                                , CreateView)
from . models import Post

def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # Default is <app>/<model>_<viewtype>.html
    context_object_name = 'posts' # Default is object_list?
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) # Directly passing context

