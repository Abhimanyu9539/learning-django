from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Post



def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blogs/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blogs/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_Posted']


class PostDetailView(DetailView):
    model = Post



def about(request):
    return render(request, 'blogs/about.html', {'title': 'About'})


