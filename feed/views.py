from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Post, Comment, Interaction
from django.contrib.auth.models import User
import json

def feed_home(request):
    posts = Post.objects.all()
    return render(request, 'feed/home.html', {'posts': posts})

def api_page(request):
    return render(request, 'feed/api.html')

# API Endpoints
@csrf_exempt
@require_http_methods(["POST"])
def create_post(request):
    data = json.loads(request.body)
    user = User.objects.get(id=data['user_id'])
    post = Post.objects.create(author=user, content=data['content'])
    return JsonResponse({'id': post.id, 'message': 'Post created'})

@csrf_exempt
@require_http_methods(["POST"])
def create_comment(request):
    data = json.loads(request.body)
    post = Post.objects.get(id=data['post_id'])
    user = User.objects.get(id=data['user_id'])
    comment = Comment.objects.create(post=post, author=user, text=data['text'])
    return JsonResponse({'id': comment.id, 'message': 'Comment created'})

@csrf_exempt
@require_http_methods(["POST"])
def create_interaction(request):
    data = json.loads(request.body)
    post = Post.objects.get(id=data['post_id'])
    user = User.objects.get(id=data['user_id'])
    interaction, created = Interaction.objects.get_or_create(
        post=post, user=user, defaults={'reaction': data['reaction']}
    )
    return JsonResponse({'id': interaction.id, 'message': 'Interaction created'})

@require_http_methods(["GET"])
def list_posts(request):
    posts = Post.objects.all().values('id', 'content', 'author__username', 'created_at')
    return JsonResponse({'posts': list(posts)})
