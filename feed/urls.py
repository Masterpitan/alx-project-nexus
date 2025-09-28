from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed_home, name='feed_home'),
    path('api/', views.api_page, name='api_page'),

    # REST API endpoints
    path('api/posts/', views.list_posts, name='list_posts'),
    path('api/posts/create/', views.create_post, name='create_post'),
    path('api/comments/create/', views.create_comment, name='create_comment'),
    path('api/interactions/create/', views.create_interaction, name='create_interaction'),
]
