from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog 1</h1>')


def about(request):
    return HttpResponse('<h1>Blog About</h1>')