from django.contrib import admin
from .models import Post, Comment, Interaction
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'content', 'created_at']
    list_filter = ['created_at', 'author']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'text', 'created_at']
    list_filter = ['created_at', 'author']

@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'reaction', 'created_at']
    list_filter = ['reaction', 'created_at']
