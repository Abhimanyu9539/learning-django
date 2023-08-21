from django.shortcuts import render
from django.http import HttpResponse

posts= [
    {
        "author":'ABD',
        "title": "Blog Post 1",
        "Content": "First Post Content",
        "date_Posted":"August 21, 2023"
    },
        {
        "author":'ABD',
        "title": "Blog Post 2",
        "Content": "Second Post Content",
        "date_Posted":"August 22, 2023"
    }
    
]

def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})