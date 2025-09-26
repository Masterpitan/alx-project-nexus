from django.shortcuts import render
from django.http import JsonResponse
from .models import Post
# Create your views here.

def feed_home(request):
    posts = Post.objects.all()
    return render(request, 'feed/home.html', {'posts': posts})

def api_page(request):
    return render(request, 'feed/api.html')
