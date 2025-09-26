import graphene
from graphene_django import DjangoObjectType
from .models import Post, Comment, Interaction


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("id", "author", "content", "created_at", "comments", "interactions")


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ("id", "post", "author", "text", "created_at")


class InteractionType(DjangoObjectType):
    class Meta:
        model = Interaction
        fields = ("id", "post", "user", "reaction", "created_at")


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)

    def resolve_all_posts(root, info):
        return Post.objects.all()


schema = graphene.Schema(query=Query)
