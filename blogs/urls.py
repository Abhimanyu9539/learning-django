from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="blog-home"),  ## Home page route
    path('about/', views.about, name="blog-about"),
]
