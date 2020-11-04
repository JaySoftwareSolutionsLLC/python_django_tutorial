from django.shortcuts import render
from django.http import HttpResponse

# Normally, we will pull this info in from db, but using hard-coded data for example data to be used with templating
posts = [
    {
        'author': 'Brett',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 1, 2020'
    },
    {
        'author': 'Brett',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 4, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) # Directly passing context